from tajik_ai_utils import cyrillic_to_latin_tajik, latin_to_cyrillic_tajik


def test_cyrillic_to_latin_tajik():
    assert cyrillic_to_latin_tajik("Салом") == "Salom"


def test_latin_to_cyrillic_tajik():
    assert latin_to_cyrillic_tajik("Salom") == "Салом"
