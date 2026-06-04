import argparse

from .dataset import clean_for_llm_dataset
from .normalize import normalize_tajik_text
from .transliterate import cyrillic_to_latin_tajik, latin_to_cyrillic_tajik


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="tajik-ai-utils",
        description="Command-line utilities for Tajik-language AI/NLP text preprocessing.",
    )

    parser.add_argument(
        "command",
        choices=[
            "normalize",
            "clean-dataset",
            "cyrillic-to-latin",
            "latin-to-cyrillic",
        ],
        help="Utility command to run.",
    )

    parser.add_argument(
        "text",
        help="Input text to process.",
    )

    args = parser.parse_args()

    if args.command == "normalize":
        output = normalize_tajik_text(args.text)
    elif args.command == "clean-dataset":
        output = clean_for_llm_dataset(args.text)
    elif args.command == "cyrillic-to-latin":
        output = cyrillic_to_latin_tajik(args.text)
    elif args.command == "latin-to-cyrillic":
        output = latin_to_cyrillic_tajik(args.text)
    else:
        raise ValueError(f"Unsupported command: {args.command}")

    print(output)


if __name__ == "__main__":
    main()
