import re

from .normalize import normalize_tajik_text


TAJIK_SPECIFIC_CHARS = set("ғҒӣӢқҚӯӮҳҲҷҶ")


def clean_for_llm_dataset(text: str, min_length: int = 2) -> str:
    """Clean Tajik text for simple LLM/RAG dataset preprocessing."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if min_length < 0:
        raise ValueError("min_length must be greater than or equal to 0")

    text = normalize_tajik_text(text)
    text = re.sub(r"[^\w\s,.!?;:—\-()«»\"']", "", text, flags=re.UNICODE)

    if len(text) < min_length:
        return ""

    return text


def is_probably_tajik_text(text: str) -> bool:
    """
    Heuristic check for Tajik Cyrillic text.

    This is not a language detector. It only checks for Tajik-specific
    Cyrillic characters that are common in Tajik writing.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return any(char in TAJIK_SPECIFIC_CHARS for char in text)
