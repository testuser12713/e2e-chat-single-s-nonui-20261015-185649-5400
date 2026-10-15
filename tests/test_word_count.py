from textutils.word_count import word_count


def test_multiple_spaces() -> None:
    assert word_count("one two  three") == 3


def test_whitespace_only() -> None:
    assert word_count("   ") == 0


def test_empty() -> None:
    assert word_count("") == 0


def test_mixed_whitespace() -> None:
    assert word_count("a\tb\nc ") == 3
