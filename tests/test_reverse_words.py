from textutils.reverse_words import reverse_words


def test_reverse_words_ac06_example() -> None:
    assert reverse_words("  the quick   brown fox ") == "fox brown quick the"


def test_reverse_words_empty() -> None:
    assert reverse_words("") == ""


def test_reverse_words_whitespace_only() -> None:
    assert reverse_words("   \t\n ") == ""


def test_reverse_words_single_word() -> None:
    assert reverse_words("hello") == "hello"
