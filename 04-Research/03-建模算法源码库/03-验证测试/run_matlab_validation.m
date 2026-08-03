function run_matlab_validation()
%RUN_MATLAB_VALIDATION Smoke-test every callable branch in the curated MATLAB library.

testRoot = fileparts(mfilename('fullpath'));
libraryRoot = fileparts(testRoot);
addpath(fullfile(libraryRoot, "02-MATLAB实现代码", "拟合与预测脚本"));
addpath(fullfile(libraryRoot, "02-MATLAB实现代码", "智能算法代码"));
addpath(fullfile(libraryRoot, "02-MATLAB实现代码", "规划求解代码"));

entries = struct('branch', {}, 'status', {}, 'detail', {});
entries(end + 1) = executeCase("evaluation/ahp", @testAHP, true, "");
entries(end + 1) = executeCase("evaluation/entropy", @testEntropy, true, "");
entries(end + 1) = executeCase("evaluation/topsis", @testTOPSIS, true, "");
entries(end + 1) = executeCase("evaluation/gra", @testGRA, true, "");
entries(end + 1) = executeCase("evaluation/fuzzy", @testFuzzy, true, "");
entries(end + 1) = executeCase("forecast/ols", @testOLS, true, "");
entries(end + 1) = executeCase("forecast/ses", @testSES, true, "");
entries(end + 1) = executeCase("forecast/gm11", @testGM11, true, "");
entries(end + 1) = executeCase("dynamics/sir", @testSIR, true, "");
entries(end + 1) = executeCase("dynamics/logistic", @testLogistic, true, "");
entries(end + 1) = executeCase("dynamics/diffusion", @testDiffusion, true, "");
entries(end + 1) = executeCase("optimization/weighted-sum", @testWeightedSum, true, "");
entries(end + 1) = executeCase("optimization/knapsack", @testKnapsack, true, "");
entries(end + 1) = executeCase("optimization/interval", @testInterval, true, "");
entries(end + 1) = executeCase("network/shortest", @testShortest, true, "");
entries(end + 1) = executeCase("network/mst", @testMST, true, "");
entries(end + 1) = executeCase("network/maxflow", @testMaxFlow, true, "");
entries(end + 1) = executeCase("queue/mm1", @testMM1, true, "");
entries(end + 1) = executeCase("metaheuristic/aco-tsp", @testACO, true, "");

hasOptimization = exist('linprog', 'file') == 2 && exist('intlinprog', 'file') == 2;
entries(end + 1) = executeCase("optimization/lp", @testLP, hasOptimization, "Optimization Toolbox 不可用");
entries(end + 1) = executeCase("optimization/milp", @testMILP, hasOptimization, "Optimization Toolbox 不可用");

hasGlobal = exist('ga', 'file') == 2 && exist('particleswarm', 'file') == 2 && ...
    exist('simulannealbnd', 'file') == 2;
entries(end + 1) = executeCase("metaheuristic/ga", @testGA, hasGlobal, "Global Optimization Toolbox 不可用");
entries(end + 1) = executeCase("metaheuristic/pso", @testPSO, hasGlobal, "Global Optimization Toolbox 不可用");
entries(end + 1) = executeCase("metaheuristic/sa", @testSA, hasGlobal, "Global Optimization Toolbox 不可用");

hasEconometrics = exist('arima', 'file') == 2 || exist('arima', 'class') == 8;
entries(end + 1) = executeCase("forecast/arima", @testARIMA, hasEconometrics, "Econometrics Toolbox 不可用");
hasDeepLearning = exist('sequenceInputLayer', 'file') == 2 && exist('lstmLayer', 'file') == 2;
entries(end + 1) = executeCase("forecast/lstm-layers", @testLSTMLayers, hasDeepLearning, "Deep Learning Toolbox 不可用");

statuses = string({entries.status});
report = struct( ...
    'generated_at', char(datetime('now', 'TimeZone', 'local', 'Format', 'yyyy-MM-dd''T''HH:mm:ssXXX')), ...
    'matlab_version', version, ...
    'release', version('-release'), ...
    'total_branches', numel(entries), ...
    'passed', sum(statuses == "passed"), ...
    'skipped', sum(statuses == "skipped"), ...
    'failed', sum(statuses == "failed"), ...
    'entries', entries);
resultPath = fullfile(testRoot, "matlab_validation_result.json");
stream = fopen(resultPath, 'w', 'n', 'UTF-8');
cleanup = onCleanup(@() fclose(stream)); %#ok<NASGU>
fprintf(stream, '%s\n', jsonencode(report, PrettyPrint=true));
fprintf('MATLAB_VALIDATION total=%d passed=%d skipped=%d failed=%d\n', ...
    report.total_branches, report.passed, report.skipped, report.failed);
if report.failed > 0
    error("MATLAB_VALIDATION_FAILED:%d", report.failed);
end
end

function entry = executeCase(name, callback, available, skipDetail)
entry = struct('branch', char(name), 'status', '', 'detail', '');
if ~available
    entry.status = 'skipped';
    entry.detail = char(skipDetail);
    return;
end
try
    callback();
    entry.status = 'passed';
    entry.detail = '小规模确定性断言通过';
catch exception
    entry.status = 'failed';
    entry.detail = char(string(exception.identifier) + ": " + string(exception.message));
end
end

function testAHP()
A = [1 2 4; 1/2 1 2; 1/4 1/2 1];
[w, CR, ok] = evaluation_models("ahp", A);
assert(abs(sum(w) - 1) < 1e-12 && CR < 0.1 && ok);
end

function testEntropy()
w = evaluation_models("entropy", [1 2 6; 2 5 4; 5 3 1]);
assert(all(w >= 0) && abs(sum(w) - 1) < 1e-12);
end

function testTOPSIS()
[score, ranking] = evaluation_models("topsis", [9 2; 6 5; 3 8], [0.6 0.4], [true false]);
assert(all(score >= 0 & score <= 1) && ranking(1) == 1);
end

function testGRA()
grade = evaluation_models("gra", [1 2; 2 3; 3 4], [3 4], 0.5);
assert(numel(grade) == 3 && grade(3) >= grade(1));
end

function testFuzzy()
B = evaluation_models("fuzzy", [0.4 0.6], [0.7 0.3; 0.2 0.8]);
assert(max(abs(B - [0.4 0.6])) < 1e-12);
end

function testOLS()
x = (1:6)'; y = 2 + 3 * x;
[beta, fitted, residual] = forecast_models("ols", x, y);
assert(max(abs(beta - [2; 3])) < 1e-10 && max(abs(fitted - y)) < 1e-10 && norm(residual) < 1e-10);
end

function testSES()
[fitted, next] = forecast_models("ses", [1 2 3 4], 0.5);
assert(isnan(fitted(1)) && abs(next - 3.125) < 1e-12);
end

function testGM11()
result = forecast_models("gm11", [3.1 3.4 3.8 4.2 4.7], 2);
assert(numel(result.fitted) == 5 && numel(result.forecast) == 2 && all(isfinite(result.forecast)));
end

function testSIR()
[t, y] = dynamics_models("sir", 0.3, 0.1, [990 10 0], [0 20]);
assert(numel(t) > 2 && max(abs(sum(y, 2) - 1000)) < 1e-5 && all(y(:) >= -1e-6));
end

function testLogistic()
[~, population] = dynamics_models("logistic", 0.4, 100, 10, [0 20]);
assert(population(end) > population(1) && population(end) < 101);
end

function testDiffusion()
history = dynamics_models("diffusion", [0 0 1 0 0], 1, 1, 0.25, 4);
assert(isequal(size(history), [5 5]) && all(isfinite(history), 'all'));
end

function testWeightedSum()
score = optimization_network_models("weighted-sum", [2 3], [0.5 0.5]);
assert(abs(score - 2.5) < 1e-12);
end

function testKnapsack()
[value, chosen] = optimization_network_models("knapsack", [6 10 12], [1 2 3], 5);
assert(value == 22 && isequal(chosen, [2 3]));
end

function testInterval()
selected = optimization_network_models("interval", [1 2 1; 2 3 2; 1 4 3; 4 5 4]);
assert(isequal(selected(:, 3)', [1 2 4]));
end

function testShortest()
[path, distance] = optimization_network_models("shortest", [1 1 2], [2 3 3], [1 4 1], 1, 3, false);
assert(isequal(path, [1 2 3]) && abs(distance - 2) < 1e-12);
end

function testMST()
[tree, weight] = optimization_network_models("mst", [1 1 2], [2 3 3], [1 4 1]);
assert(numedges(tree) == 2 && abs(weight - 2) < 1e-12);
end

function testMaxFlow()
[flow, ~, ~, ~] = optimization_network_models("maxflow", [1 1 2 2 3], [2 3 3 4 4], [3 2 1 2 3], 1, 4);
assert(abs(flow - 5) < 1e-12);
end

function testMM1()
result = optimization_network_models("mm1", 2, 3);
assert(abs(result.rho - 2/3) < 1e-12 && abs(result.L - 2) < 1e-12);
end

function testACO()
distance = [0 1 sqrt(2) 1; 1 0 1 sqrt(2); sqrt(2) 1 0 1; 1 sqrt(2) 1 0];
[route, lengthValue, history] = metaheuristics("aco-tsp", distance, 16, 30, 42);
assert(numel(route) == 5 && abs(lengthValue - 4) < 1e-10 && all(diff(history) <= 1e-12));
end

function testLP()
[x, fval] = optimization_network_models("lp", [1; 2], [-1 -1], -1, [], [], [0; 0], []);
assert(abs(fval - 1) < 1e-7 && abs(sum(x) - 1) < 1e-7);
end

function testMILP()
[x, fval] = optimization_network_models("milp", [1; 2], [1 2], [-1 -1], -1, [], [], [0; 0], [1; 1]);
assert(abs(fval - 1) < 1e-7 && abs(sum(x) - 1) < 1e-7);
end

function testGA()
[~, fval] = metaheuristics("ga", @(x) sum(x.^2), [-5 -5], [5 5], 42);
assert(fval < 1e-3);
end

function testPSO()
[~, fval] = metaheuristics("pso", @(x) sum(x.^2), [-5 -5], [5 5], 42);
assert(fval < 1e-3);
end

function testSA()
[~, fval] = metaheuristics("sa", @(x) sum(x.^2), [2 2], [-5 -5], [5 5], 42);
assert(fval < 0.5);
end

function testARIMA()
rng(42, 'twister');
y = cumsum(randn(60, 1));
result = forecast_models("arima", y, [1 1 0], 3);
assert(numel(result.mean) == 3 && all(isfinite(result.mean)));
end

function testLSTMLayers()
layers = forecast_models("lstm-layers", 2, 8);
assert(numel(layers) == 4);
end
