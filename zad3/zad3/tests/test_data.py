import pytest
from my_lib.data import chunk, safe_get


def test_chunk_basic():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_invalid_size():
    with pytest.raises(ValueError):
        chunk([1, 2], 0)


def test_safe_get_found():
    assert safe_get({"a": 1}, "a") == 1


def test_safe_get_default():
    assert safe_get({"a": 1}, "b", 99) == 99


def test_safe_get_wrong_type():
    with pytest.raises(TypeError):
        safe_get([1, 2, 3], "a")
