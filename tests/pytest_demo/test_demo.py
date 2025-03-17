from src.pytest_demo.demo import min_max_exceeded


def test_demo():
    assert min_max_exceeded(5, 0, 1)
