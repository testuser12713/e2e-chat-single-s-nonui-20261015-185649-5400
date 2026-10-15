"""Return True if text reads the same forwards and backwards."""


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards."""
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]
