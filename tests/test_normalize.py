from tajik_ai_utils import normalize_tajik_text


def test_normalize_tajik_text():
    assert normalize_tajik_text("  Салом    дунё!!!  ") == "Салом дунё!"
