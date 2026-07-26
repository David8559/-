function varargout = optimization_network_models(method, varargin)
%OPTIMIZATION_NETWORK_MODELS 规划、图论、排队论与基础算法统一入口。

switch lower(string(method))
    case "lp"
        [varargout{1:nargout}] = solveLP(varargin{:});
    case "milp"
        [varargout{1:nargout}] = solveMILP(varargin{:});
    case "weighted-sum"
        varargout{1} = weightedSum(varargin{:});
    case "knapsack"
        [varargout{1:nargout}] = knapsack01(varargin{:});
    case "interval"
        varargout{1} = intervalGreedy(varargin{:});
    case "shortest"
        [varargout{1:nargout}] = graphShortest(varargin{:});
    case "mst"
        [varargout{1:nargout}] = graphMST(varargin{:});
    case "maxflow"
        [varargout{1:nargout}] = graphMaxFlow(varargin{:});
    case "mm1"
        varargout{1} = mm1(varargin{:});
    otherwise
        error("未知方法：%s", method);
end
end

function [x, fval, exitflag, output] = solveLP(f, A, b, Aeq, beq, lb, ub)
options = optimoptions("linprog", Display="none");
[x, fval, exitflag, output] = linprog(f, A, b, Aeq, beq, lb, ub, options);
if exitflag <= 0
    error("LP 未成功收敛：%s", output.message);
end
end

function [x, fval, exitflag, output] = solveMILP(f, intcon, A, b, Aeq, beq, lb, ub)
options = optimoptions("intlinprog", Display="off");
[x, fval, exitflag, output] = intlinprog(f, intcon, A, b, Aeq, beq, lb, ub, options);
if exitflag <= 0
    error("MILP 未成功收敛：%s", output.message);
end
end

function score = weightedSum(values, weights, ideal, nadir)
weights = weights(:) / sum(weights);
values = values(:);
if nargin >= 4
    if any(nadir(:) <= ideal(:))
        error("nadir 必须逐项大于 ideal");
    end
    values = (values - ideal(:)) ./ (nadir(:) - ideal(:));
end
score = weights' * values;
end

function [bestValue, chosen] = knapsack01(values, weights, capacity)
values = values(:); weights = weights(:);
n = numel(values);
if numel(weights) ~= n || any(weights <= 0) || capacity < 0
    error("价值/重量长度需一致，重量为正，容量非负");
end
dp = zeros(n + 1, capacity + 1);
for i = 1:n
    dp(i + 1, :) = dp(i, :);
    for c = weights(i):capacity
        dp(i + 1, c + 1) = max(dp(i + 1, c + 1), ...
            dp(i, c - weights(i) + 1) + values(i));
    end
end
chosen = [];
c = capacity;
for i = n:-1:1
    if abs(dp(i + 1, c + 1) - dp(i, c + 1)) > 1e-12
        chosen = [i, chosen]; %#ok<AGROW>
        c = c - weights(i);
    end
end
bestValue = dp(n + 1, capacity + 1);
end

function selected = intervalGreedy(intervals)
% intervals 每行：[start, finish, id]。
intervals = sortrows(intervals, 2);
selected = zeros(0, size(intervals, 2));
lastEnd = -Inf;
for i = 1:size(intervals, 1)
    if intervals(i, 2) < intervals(i, 1)
        error("区间结束时间不能早于开始时间");
    end
    if intervals(i, 1) >= lastEnd
        selected(end + 1, :) = intervals(i, :); %#ok<AGROW>
        lastEnd = intervals(i, 2);
    end
end
end

function [path, distance] = graphShortest(s, t, weights, source, target, directed)
if nargin < 6
    directed = false;
end
if directed
    G = digraph(s, t, weights);
else
    G = graph(s, t, weights);
end
[path, distance] = shortestpath(G, source, target);
end

function [T, totalWeight] = graphMST(s, t, weights)
G = graph(s, t, weights);
T = minspantree(G, Method="sparse");
totalWeight = sum(T.Edges.Weight);
end

function [flowValue, flowGraph, sourceSide, sinkSide] = graphMaxFlow(s, t, capacity, source, sink)
G = digraph(s, t, capacity);
[flowValue, flowGraph, sourceSide, sinkSide] = maxflow(G, source, sink);
end

function result = mm1(lambda, mu)
if lambda < 0 || mu <= lambda
    error("稳态 M/M/1 必须满足 0 <= lambda < mu");
end
rho = lambda / mu;
result = struct( ...
    'rho', rho, ...
    'L', rho / (1 - rho), ...
    'Lq', rho^2 / (1 - rho), ...
    'W', 1 / (mu - lambda), ...
    'Wq', lambda / (mu * (mu - lambda)));
end
