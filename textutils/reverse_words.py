"""Reverse the order of the words in text."""


def reverse_words(text: str) -> str:
    """Reverse the order of the words in text."""
    return " ".join(reversed(text.split()))
