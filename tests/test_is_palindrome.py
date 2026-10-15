from textutils.is_palindrome import is_palindrome


def test_sentence_palindrome() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome() -> None:
    assert is_palindrome("hello") is False


def test_empty() -> None:
    assert is_palindrome("") is True


def test_punctuation_only() -> None:
    assert is_palindrome("!?, ") is True
