from textutils.slugify import slugify


def test_basic() -> None:
    assert slugify("Hello, World!") == "hello-world"


def test_accents() -> None:
    assert slugify("  Crème Brûlée  ") == "creme-brulee"


def test_only_symbols() -> None:
    assert slugify("!!!") == ""


def test_empty_and_collapse() -> None:
    assert slugify("") == ""
    assert slugify("a --  b__c") == "a-b-c"
