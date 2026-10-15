# textutils

`textutils` ist eine kleine, abhängigkeitsfreie Python-Bibliothek mit fünf Zeichenketten-Helfern: `slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`. Es gibt keine Oberfläche und keine Datenspeicherung.

## Tech-Stack

- Python 3.10+
- Paketierung: `pyproject.toml` (setuptools)
- Tests: pytest
- Lint: ruff

## Installation

```bash
pip install -e .[dev]
```

## Tests und Lint

```bash
pytest
ruff check .
```

## Verwendung / API

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

- `slugify(text: str) -> str` – erzeugt einen URL-tauglichen Slug.
- `truncate(text: str, max_len: int) -> str` – kürzt Text auf `max_len` Zeichen (`ValueError` bei `max_len < 0`).
- `word_count(text: str) -> int` – zählt die Wörter.
- `is_palindrome(text: str) -> bool` – prüft auf Palindrom.
- `reverse_words(text: str) -> str` – kehrt die Wortreihenfolge um.

## Funktionen

- Fünf unabhängige String-Helfer ohne Laufzeit-Abhängigkeiten
- Ein Unit-Test pro Funktion
