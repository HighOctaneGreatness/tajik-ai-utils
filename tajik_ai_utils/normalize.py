from .clean import normalize_punctuation, remove_extra_spaces


TAJIK_CHAR_REPLACEMENTS = {
    "ي": "ӣ",
    "ӣ̀": "ӣ",
}


def normalize_tajik_text(text: str) -> str:
    """
    Normalize Tajik text for basic AI/NLP preprocessing.

    This function intentionally stays conservative:
    it avoids aggressive linguistic corrections and focuses on cleanup
    that is safe for datasets, search and chatbot preprocessing.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for source, target in TAJIK_CHAR_REPLACEMENTS.items():
        text = text.replace(source, target)

    text = normalize_punctuation(text)
    text = remove_extra_spaces(text)

    return text
