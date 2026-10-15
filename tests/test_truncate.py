import pytest

from textutils.truncate import truncate


def test_short_text_unchanged() -> None:
    assert truncate("hello", 10) == "hello"


def test_exact_length_unchanged() -> None:
    assert truncate("hello", 5) == "hello"


def test_long_text_truncated() -> None:
    assert truncate("hello world", 5) == "hell…"


def test_zero_returns_empty() -> None:
    assert truncate("abc", 0) == ""


def test_negative_raises() -> None:
    with pytest.raises(ValueError):
        truncate("abc", -1)
