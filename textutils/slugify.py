"""Convert text to a URL-friendly slug."""

import re
import unicodedata


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
