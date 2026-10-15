import textutils
from textutils import is_palindrome, reverse_words, slugify, truncate, word_count

NAMES = ["slugify", "truncate", "word_count", "is_palindrome", "reverse_words"]


def test_all_names_importable_and_callable():
    for fn in (slugify, truncate, word_count, is_palindrome, reverse_words):
        assert callable(fn)


def test_all_lists_exactly_five_names():
    assert sorted(textutils.__all__) == sorted(NAMES)
