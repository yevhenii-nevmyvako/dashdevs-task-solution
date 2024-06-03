import pytest
from equilibrium_index_finder.core.base import find_index


@pytest.fixture
def test_cases():
    return [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3, 4, 3, 2, 1], 3),
        ([1, 2, 3, 4, 5, 6], -1),
        ([2, 1, -1, 1, 2], 1),
        ([-7, 1, 5, 2, -4, 3, 0], 3),
    ]


def test_find_equilibrium_index(test_cases):
    for i, (arr, expected) in enumerate(test_cases):
        result = find_index(arr)
        assert result == expected, f'Test case {i + 1} failed: expected {expected}, got {result}'
