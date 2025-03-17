import pytest

from src.pytest_demo.demo import min_max_exceeded


@pytest.mark.parametrize(
    'value, expected', [
        (-3, True),
        (-2, True),
        (-1, True),
        (0, True),
        (1, False),
        (2, False),
        (3, False),
        (4, False),
        (5, True),
        (6, True),
    ])
def test_invalid_and_or_queries(value, expected):
    assert min_max_exceeded(value, 0, 5) == expected
