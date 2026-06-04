from tajik_ai_utils import normalize_punctuation, remove_extra_spaces


def test_remove_extra_spaces():
    assert remove_extra_spaces("  Салом    дунё  ") == "Салом дунё"


def test_normalize_punctuation():
    assert normalize_punctuation("Салом!!!Дунё??") == "Салом! Дунё?"
