# Tajik AI Utils

**Tajik AI Utils** is an open-source Python toolkit for cleaning, normalizing and preparing Tajik-language text for AI, NLP, search, RAG systems and dataset workflows.

Tajik is a low-resource language in modern AI tooling. This project aims to provide practical utilities for developers, researchers and educators working with Tajik Cyrillic, mixed-script text and AI datasets.

## Features

- Tajik Cyrillic text normalization
- Extra whitespace cleanup
- Punctuation cleanup
- Dataset text cleaning for LLM and RAG workflows
- Tajik Cyrillic to Latin transliteration
- Tajik Latin to Cyrillic transliteration
- Simple preprocessing utilities for search and chatbots

## Why this project matters

Many AI and NLP libraries focus primarily on English and other high-resource languages. Tajik-language developers often need custom preprocessing tools before they can build chatbots, search tools, educational software, OCR pipelines, RAG systems or local datasets.

This project focuses on small, readable and reusable building blocks for Tajik text processing.

## Installation

```bash
pip install tajik-ai-utils
```

## For local development

```bash
git clone https://github.com/HighOctaneGreatness/tajik-ai-utils.git
cd tajik-ai-utils
pip install -e ".[dev]"
```

## Usage

```python
from tajik_ai_utils import (
    normalize_tajik_text,
    clean_for_llm_dataset,
    cyrillic_to_latin_tajik,
    latin_to_cyrillic_tajik,
)

text = "  Салом    дунё!!!  Ин   як   матни   тоҷикӣ аст.  "

print(normalize_tajik_text(text))
print(clean_for_llm_dataset(text))
print(cyrillic_to_latin_tajik("Салом Тоҷикистон"))
print(latin_to_cyrillic_tajik("Salom Tojikiston"))
```
