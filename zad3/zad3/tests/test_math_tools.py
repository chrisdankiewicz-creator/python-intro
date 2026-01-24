import pytest
from my_lib.math_tools import add, clamp, mean


def test_add():
    assert add(2, 3) == 5


def test_clamp_in_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_low():
    assert clamp(-1, 0, 10) == 0


def test_clamp_high():
    assert clamp(99, 0, 10) == 10


def test_clamp_bad_range():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_mean_basic():
    assert mean([1, 2, 3]) == 2


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])
