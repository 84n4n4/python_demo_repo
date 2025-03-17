from random import randint

import pytest

from src.pytest_demo.demo import min_max_exceeded


def make_params():
    return [randint(-1000, 1000) for _ in range(1000)]

def oracle(value):
    return value <= 0 or value >= 5

@pytest.fixture(params=make_params())
def param_set(request):
    return request.param


def test_invalid_and_or_queries(param_set):
    value = param_set
    assert min_max_exceeded(value, 0, 5) == oracle(value)
