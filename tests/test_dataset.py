from tajik_ai_utils import clean_for_llm_dataset, is_probably_tajik_text


def test_clean_for_llm_dataset():
    assert clean_for_llm_dataset("  Салом!!!  ") == "Салом!"


def test_is_probably_tajik_text():
    assert is_probably_tajik_text("Тоҷикистон") is True
    assert is_probably_tajik_text("Salom") is False
