import pytest
from my_lib.Tekst import word_count, is_palindrome, slugify


def test_word_count():
    assert word_count("ala ma kota") == 3


def test_word_count_type_error():
    with pytest.raises(TypeError):
        word_count(123)  # type: ignore


def test_is_palindrome():
    assert is_palindrome("Kajak") is True
    assert is_palindrome("Hej") is False


def test_slugify():
    assert slugify("Hello World!") == "hello-world"
