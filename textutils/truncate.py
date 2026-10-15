"""Truncate text to at most max_len characters, ending with an ellipsis."""


def truncate(text: str, max_len: int) -> str:
    """Truncate text to at most max_len characters, ending with an ellipsis."""
    if max_len < 0:
        raise ValueError("max_len must be >= 0")
    if len(text) <= max_len:
        return text
    if max_len == 0:
        return ""
    return text[: max_len - 1] + "…"
