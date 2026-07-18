import importlib.util
import importlib


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_three_sum_cases():
    ts = load_module('src/26_06_20_three_sum.py', 'ts')
    assert ts.solution([0, 0, 0, 0]) == 4
    assert ts.solution([-1, 0, 1]) == 1
    assert ts.solution([-1, 0, 1, 2, -1, -4]) == 2
