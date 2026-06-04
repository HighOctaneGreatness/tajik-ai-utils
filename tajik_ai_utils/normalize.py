import re


def remove_extra_spaces(text: str) -> str:
    """Remove repeated whitespace and trim text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return re.sub(r"\s+", " ", text).strip()


def normalize_punctuation(text: str) -> str:
    """Normalize common repeated punctuation patterns."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = re.sub(r"!{2,}", "!", text)
    text = re.sub(r"\?{2,}", "?", text)
    text = re.sub(r"\.{4,}", "...", text)
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)
    text = re.sub(r"([,.!?;:])([^\s])", r"\1 \2", text)

    return remove_extra_spaces(text)
