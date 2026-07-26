function varargout = metaheuristics(method, varargin)
%METAHEURISTICS MATLAB 全局优化算法统一入口。
% GA/PSO/SA 需要 Global Optimization Toolbox；ACO 为本文件实现。
% 所有目标均按“越小越好”，正式报告应固定 rng 并进行多随机种子重复。

switch lower(string(method))
    case "ga"
        [varargout{1:nargout}] = runGA(varargin{:});
    case "pso"
        [varargout{1:nargout}] = runPSO(varargin{:});
    case "sa"
        [varargout{1:nargout}] = runSA(varargin{:});
    case "aco-tsp"
        [varargout{1:nargout}] = acoTSP(varargin{:});
    otherwise
        error("未知方法：%s", method);
end
end

function [x, fval, output] = runGA(objective, lb, ub, seed)
if nargin < 4
    seed = 42;
end
rng(seed, "twister");
nvars = numel(lb);
options = optimoptions("ga", Display="off", PopulationSize=80, ...
    MaxGenerations=200, UseParallel=false);
[x, fval, ~, output] = ga(objective, nvars, [], [], [], [], lb, ub, [], options);
end

function [x, fval, output] = runPSO(objective, lb, ub, seed)
if nargin < 4
    seed = 42;
end
rng(seed, "twister");
nvars = numel(lb);
options = optimoptions("particleswarm", Display="off", SwarmSize=60, ...
    MaxIterations=200, UseParallel=false);
[x, fval, ~, output] = particleswarm(objective, nvars, lb, ub, options);
end

function [x, fval, output] = runSA(objective, initial, lb, ub, seed)
if nargin < 5
    seed = 42;
end
rng(seed, "twister");
options = optimoptions("simulannealbnd", Display="off", MaxIterations=1000);
[x, fval, ~, output] = simulannealbnd(objective, initial, lb, ub, options);
end

function [bestRoute, bestLength, history] = acoTSP(distance, ants, iterations, seed)
if nargin < 2, ants = 40; end
if nargin < 3, iterations = 150; end
if nargin < 4, seed = 42; end
rng(seed, "twister");
n = size(distance, 1);
if size(distance, 2) ~= n || any(distance < 0, 'all') || ...
        max(abs(distance - distance'), [], 'all') > 1e-10
    error("distance 必须为非负对称方阵");
end
offDiagonal = ~eye(n);
if any(abs(diag(distance)) > 1e-12) || any(distance(offDiagonal) <= 0)
    error("distance 对角线必须为 0，非对角元素必须为正");
end
alpha = 1; beta = 3; evaporation = 0.5;
heuristic = zeros(n);
mask = distance > 0;
heuristic(mask) = 1 ./ distance(mask);
pheromone = ones(n);
bestRoute = [];
bestLength = Inf;
history = zeros(iterations, 1);

for iteration = 1:iterations
    routes = zeros(ants, n + 1);
    lengths = zeros(ants, 1);
    for ant = 1:ants
        start = randi(n);
        route = start;
        unvisited = setdiff(1:n, start);
        while ~isempty(unvisited)
            current = route(end);
            desirability = pheromone(current, unvisited).^alpha .* ...
                heuristic(current, unvisited).^beta;
            if sum(desirability) <= 0
                idx = randi(numel(unvisited));
            else
                probability = desirability / sum(desirability);
                idx = find(rand <= cumsum(probability), 1);
            end
            next = unvisited(idx);
            route(end + 1) = next; %#ok<AGROW>
            unvisited(idx) = [];
        end
        route(end + 1) = start;
        edgeIndex = sub2ind([n n], route(1:end-1), route(2:end));
        lengthValue = sum(distance(edgeIndex));
        routes(ant, :) = route;
        lengths(ant) = lengthValue;
        if lengthValue < bestLength
            bestRoute = route;
            bestLength = lengthValue;
        end
    end
    pheromone = (1 - evaporation) * pheromone;
    for ant = 1:ants
        deposit = 1 / max(lengths(ant), eps);
        for k = 1:n
            i = routes(ant, k); j = routes(ant, k + 1);
            pheromone(i, j) = pheromone(i, j) + deposit;
            pheromone(j, i) = pheromone(j, i) + deposit;
        end
    end
    history(iteration) = bestLength;
end
end
