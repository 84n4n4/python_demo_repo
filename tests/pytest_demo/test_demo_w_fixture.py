import pytest

from src.pytest_demo.demo import min_max_exceeded


@pytest.fixture(scope="module", autouse=True)
def my_fixture():
    print('INITIALIZATION')
    yield
    print('TEAR DOWN')

def test_demo_f1():
    print('\nTEST F1')
    assert min_max_exceeded(5, 0, 1)

def test_demo_f2():
    print('\nTEST F2')
    assert not min_max_exceeded(0.5, 0, 1)