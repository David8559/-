function varargout = dynamics_models(method, varargin)
%DYNAMICS_MODELS SIR、Logistic 与一维扩散模型统一入口。

switch lower(string(method))
    case "sir"
        [varargout{1:nargout}] = sirSolve(varargin{:});
    case "logistic"
        [varargout{1:nargout}] = logisticSolve(varargin{:});
    case "diffusion"
        varargout{1} = diffuseExplicit(varargin{:});
    otherwise
        error("未知方法：%s", method);
end
end

function [t, y] = sirSolve(beta, gamma, initial, tspan)
initial = initial(:);
population = sum(initial);
rhs = @(~, state) [ ...
    -beta * state(1) * state(2) / population; ...
     beta * state(1) * state(2) / population - gamma * state(2); ...
     gamma * state(2)];
options = odeset(RelTol=1e-8, AbsTol=1e-10);
[t, y] = ode45(rhs, tspan, initial, options);
end

function [t, N] = logisticSolve(r, K, N0, tspan)
if r <= 0 || K <= 0 || N0 <= 0
    error("r、K、N0 必须为正");
end
rhs = @(~, n) r * n .* (1 - n ./ K);
[t, N] = ode45(rhs, tspan, N0, odeset(RelTol=1e-8, AbsTol=1e-10));
end

function history = diffuseExplicit(initial, D, dx, dt, steps)
u = initial(:)';
ratio = D * dt / dx^2;
if numel(u) < 3 || any([D, dx, dt, steps] <= 0)
    error("输入与网格参数无效");
end
if ratio > 0.5
    error("显式格式不稳定：需要 D*dt/dx^2 <= 0.5");
end
history = zeros(steps + 1, numel(u));
history(1, :) = u;
for k = 1:steps
    next = u;
    next(2:end-1) = u(2:end-1) + ratio * ...
        (u(3:end) - 2 * u(2:end-1) + u(1:end-2));
    u = next;
    history(k + 1, :) = u;
end
end
