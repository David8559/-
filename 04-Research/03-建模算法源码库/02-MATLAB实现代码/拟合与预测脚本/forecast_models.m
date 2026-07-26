function varargout = forecast_models(method, varargin)
%FORECAST_MODELS 预测模型统一入口。
% 时序任务必须按时间切分训练/验证集，不能随机打乱。

switch lower(string(method))
    case "ols"
        [varargout{1:nargout}] = olsFit(varargin{:});
    case "ses"
        [varargout{1:nargout}] = simpleExponentialSmoothing(varargin{:});
    case "gm11"
        varargout{1} = gm11(varargin{:});
    case "arima"
        varargout{1} = arimaForecast(varargin{:});
    case "lstm-layers"
        varargout{1} = lstmLayers(varargin{:});
    otherwise
        error("未知方法：%s", method);
end
end

function [beta, fitted, residual] = olsFit(X, y)
y = y(:);
if size(X, 1) ~= numel(y)
    error("X 行数必须等于 y 长度");
end
design = [ones(size(X, 1), 1), X];
if rank(design) < size(design, 2)
    error("设计矩阵秩亏：检查完全共线性");
end
beta = design \ y;
fitted = design * beta;
residual = y - fitted;
end

function [fitted, nextForecast] = simpleExponentialSmoothing(y, alpha)
y = y(:);
validateattributes(alpha, {'numeric'}, {'scalar','>',0,'<=',1});
if numel(y) < 2
    error("至少需要 2 个观测");
end
level = zeros(size(y));
level(1) = y(1);
for t = 2:numel(y)
    level(t) = alpha * y(t) + (1 - alpha) * level(t - 1);
end
fitted = [NaN; level(1:end-1)];
nextForecast = level(end);
end

function result = gm11(x0, horizon)
x0 = x0(:);
if nargin < 2
    horizon = 1;
end
if numel(x0) < 4 || any(x0 <= 0) || horizon < 1
    error("GM(1,1) 至少需要 4 个正数观测，horizon >= 1");
end
x1 = cumsum(x0);
z1 = 0.5 * (x1(2:end) + x1(1:end-1));
params = [-z1, ones(numel(z1), 1)] \ x0(2:end);
a = params(1); b = params(2);
if abs(a) < 1e-12
    error("发展系数接近 0，经典响应式不稳定");
end
k = (0:numel(x0) + horizon - 1)';
x1Hat = (x0(1) - b / a) .* exp(-a .* k) + b / a;
x0Hat = [x0(1); diff(x1Hat)];
residual = x0 - x0Hat(1:numel(x0));
result = struct( ...
    'a', a, 'b', b, ...
    'fitted', x0Hat(1:numel(x0)), ...
    'forecast', x0Hat(numel(x0)+1:end), ...
    'posteriorRatioC', std(residual) / std(x0));
end

function result = arimaForecast(y, order, horizon)
% 需要 Econometrics Toolbox。order = [p d q]。
y = y(:);
Mdl = arima(order(1), order(2), order(3));
EstMdl = estimate(Mdl, y, 'Display', 'off');
[meanForecast, mse] = forecast(EstMdl, horizon, 'Y0', y);
result = struct('model', EstMdl, 'mean', meanForecast, ...
    'lower95', meanForecast - 1.96 * sqrt(mse), ...
    'upper95', meanForecast + 1.96 * sqrt(mse));
end

function layers = lstmLayers(numFeatures, numHidden)
% 需要 Deep Learning Toolbox；用于单步回归。
if nargin < 2
    numHidden = 32;
end
layers = [
    sequenceInputLayer(numFeatures)
    lstmLayer(numHidden, OutputMode="last")
    fullyConnectedLayer(1)
    regressionLayer
];
end
