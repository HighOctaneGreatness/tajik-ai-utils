# Limitations

Tajik AI Utils is an early-stage project. The current implementation focuses on practical and conservative text preprocessing rather than full linguistic analysis.

## Current limitations

- Transliteration is rule-based and may not cover every real-world spelling convention.
- Latin-to-Cyrillic transliteration can be ambiguous.
- The package is not a full Tajik language detector.
- Dataset cleaning is intentionally conservative and may need project-specific tuning.
- Sentence splitting and chunking examples are simple and not yet Tajik-aware.
- OCR cleanup is not yet implemented.

## Design approach

The project avoids aggressive automatic corrections because incorrect normalization can damage datasets, search indexes and RAG pipelines.

The goal is to provide clear, predictable and testable utilities that developers can adapt to their own Tajik-language workflows.

## Planned improvements

- More transliteration test cases
- Better mixed-script handling
- Tajik-aware sentence splitting
- OCR cleanup utilities
- CLI improvements
- More documentation in Tajik and Russian
