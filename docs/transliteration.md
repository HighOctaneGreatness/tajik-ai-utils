# Tajik Transliteration

Tajik AI Utils includes simple rule-based transliteration helpers for converting between Tajik Cyrillic and a Latin representation.

The current implementation is intentionally conservative and predictable. It is designed for practical preprocessing, examples, search utilities and AI/NLP dataset preparation rather than official linguistic standardization.

## Supported functions

```python
from tajik_ai_utils import cyrillic_to_latin_tajik, latin_to_cyrillic_tajik


print(cyrillic_to_latin_tajik("Салом Тоҷикистон"))
print(latin_to_cyrillic_tajik("Salom Tojikiston"))
```

## Tajik Cyrillic examples

| Cyrillic | Latin |
|---|---|
| Салом | Salom |
| Тоҷикистон | Tojikiston |
| Ғафур | Ghafur |
| Қурбон | Qurbon |
| Ҷаҳон | Jahon |
| Ҳисор | Hisor |
| Хуҷанд | Khujand |

## Current approach

The transliteration module uses explicit character mappings for Tajik Cyrillic letters, including:

- Ғ / ғ
- Қ / қ
- Ҷ / ҷ
- Ҳ / ҳ
- Ӯ / ӯ
- Ӣ / ӣ

This makes behavior easy to inspect, test and modify.

## Known limitations

Latin-to-Cyrillic transliteration is inherently ambiguous. The same Latin spelling can sometimes map to different Cyrillic forms depending on context, pronunciation or convention.

Current limitations:

- no context-aware disambiguation
- no official standard selection yet
- no support for multiple transliteration styles
- no automatic mixed-script detection
- limited handling of proper names and dialectal spellings

## Planned improvements

Future versions may add:

- more test cases for names and places
- optional transliteration styles
- mixed-script detection helpers
- better documentation in Tajik and Russian
- comparison with common Tajik transliteration conventions
