import importlib.util
import importlib


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_hall_of_fame_example():
    hof = load_module('src/26_07_01_hall_of_fame.py', 'hof')
    assert hof.solution(3, [10, 100, 20, 150, 1, 100, 200]) == [10, 10, 10, 20, 20, 100, 100]
