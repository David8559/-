function varargout = evaluation_models(method, varargin)
%EVALUATION_MODELS 评价类模型统一入口。
% 行表示方案，列表示指标。示例：
%   [w, CR, ok] = evaluation_models("ahp", A);
%   [score, rank] = evaluation_models("topsis", X, w, benefitMask);

switch lower(string(method))
    case "ahp"
        [varargout{1:nargout}] = ahpWeights(varargin{:});
    case "entropy"
        varargout{1} = entropyWeights(varargin{:});
    case "topsis"
        [varargout{1:nargout}] = topsisScore(varargin{:});
    case "gra"
        varargout{1} = greyRelationalGrade(varargin{:});
    case "fuzzy"
        varargout{1} = fuzzyEvaluation(varargin{:});
    otherwise
        error("未知方法：%s", method);
end
end

function [w, CR, ok] = ahpWeights(A)
validateattributes(A, {'numeric'}, {'2d','square','positive','finite'});
n = size(A, 1);
if max(abs(A .* A' - 1), [], 'all') > 1e-6
    error("判断矩阵必须满足 a_ij * a_ji = 1");
end
[V, D] = eig(A);
[lambdaMax, idx] = max(real(diag(D)));
w = abs(real(V(:, idx)));
w = w / sum(w);
RI = [0 0 0.58 0.90 1.12 1.24 1.32 1.41 1.45 1.49 1.51 1.48 1.56 1.57 1.59];
if n <= 2
    CR = 0;
elseif n <= numel(RI)
    CI = (lambdaMax - n) / (n - 1);
    CR = CI / RI(n);
else
    CR = NaN;
end
ok = isnan(CR) || CR < 0.10;
end

function w = entropyWeights(X)
validateattributes(X, {'numeric'}, {'2d','nonnegative','finite','nonempty'});
if any(sum(X, 1) == 0)
    error("存在全零指标列");
end
P = X ./ sum(X, 1);
P(P == 0) = eps;
if size(X, 1) == 1
    w = ones(1, size(X, 2)) / size(X, 2);
    return;
end
e = -sum(P .* log(P), 1) / log(size(X, 1));
d = 1 - e;
w = d / sum(d);
end

function [score, rankIndex] = topsisScore(X, w, benefitMask)
validateattributes(X, {'numeric'}, {'2d','finite','nonempty'});
w = w(:)' / sum(w);
if nargin < 3
    benefitMask = true(1, size(X, 2));
else
    benefitMask = logical(benefitMask(:)');
end
if numel(w) ~= size(X, 2) || numel(benefitMask) ~= size(X, 2)
    error("权重和指标方向长度必须等于指标数");
end
denom = vecnorm(X, 2, 1);
if any(denom == 0)
    error("存在零范数指标列");
end
Z = (X ./ denom) .* w;
positive = max(Z, [], 1);
negative = min(Z, [], 1);
positive(~benefitMask) = min(Z(:, ~benefitMask), [], 1);
negative(~benefitMask) = max(Z(:, ~benefitMask), [], 1);
dPos = vecnorm(Z - positive, 2, 2);
dNeg = vecnorm(Z - negative, 2, 2);
score = dNeg ./ max(dPos + dNeg, eps);
[~, rankIndex] = sort(score, 'descend');
end

function grade = greyRelationalGrade(X, reference, rho)
validateattributes(X, {'numeric'}, {'2d','finite','nonempty'});
if nargin < 2 || isempty(reference)
    reference = max(X, [], 1);
end
if nargin < 3
    rho = 0.5;
end
validateattributes(rho, {'numeric'}, {'scalar','>',0,'<',1});
delta = abs(X - reference(:)');
dMin = min(delta, [], 'all');
dMax = max(delta, [], 'all');
if dMax == 0
    grade = ones(size(X, 1), 1);
else
    coefficient = (dMin + rho * dMax) ./ (delta + rho * dMax);
    grade = mean(coefficient, 2);
end
end

function B = fuzzyEvaluation(w, R)
w = w(:)';
if numel(w) ~= size(R, 1) || any(w < 0) || abs(sum(w) - 1) > 1e-6
    error("权重需非负、和为 1，且长度等于因素数");
end
if any(R < 0, 'all') || any(abs(sum(R, 2) - 1) > 1e-6)
    error("隶属度矩阵每行应非负且和为 1");
end
B = w * R;
B = B / sum(B);
end
