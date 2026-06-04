# Tajik RAG Preprocessing Example

This guide shows how Tajik AI Utils can be used to prepare Tajik-language text for Retrieval-Augmented Generation workflows.

RAG systems usually require clean, consistent and searchable text before creating embeddings. For low-resource languages such as Tajik, preprocessing is especially important because source data may contain inconsistent spacing, punctuation, mixed scripts or OCR artifacts.

## Basic workflow

```python
from tajik_ai_utils import clean_for_llm_dataset, normalize_tajik_text


raw_text = """
  Салом    дунё!!!  Ин   як   матни   тоҷикӣ аст.
  Ин матн метавонад барои ҷустуҷӯ, embedding ва RAG истифода шавад.
"""

normalized = normalize_tajik_text(raw_text)
cleaned = clean_for_llm_dataset(normalized)

print(cleaned)
```

## Simple chunking example

```python
from tajik_ai_utils import clean_for_llm_dataset


def chunk_text(text: str, max_chars: int = 500) -> list[str]:
    cleaned = clean_for_llm_dataset(text)
    sentences = cleaned.split(". ")

    chunks = []
    current = ""

    for sentence in sentences:
        candidate = f"{current}. {sentence}".strip(". ")

        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = sentence

    if current:
        chunks.append(current)

    return chunks


text = "Салом дунё. Ин як мисоли матни тоҷикӣ барои RAG мебошад."
print(chunk_text(text, max_chars=60))
```

## Why preprocessing matters

Clean preprocessing can improve:

- text search quality
- embedding consistency
- chunk quality
- retrieval accuracy
- downstream chatbot responses

## Planned improvements

Future versions may include:

- Tajik-aware sentence splitting
- better mixed-script detection
- OCR cleanup utilities
- dataset validation helpers
- examples for vector databases
