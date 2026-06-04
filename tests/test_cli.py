import subprocess
import sys


def run_cli(*args: str) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "tajik_ai_utils.cli", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def test_cli_normalize():
    assert run_cli("normalize", "  Салом    дунё!!!  ") == "Салом дунё!"


def test_cli_cyrillic_to_latin():
    assert run_cli("cyrillic-to-latin", "Салом") == "Salom"


def test_cli_latin_to_cyrillic():
    assert run_cli("latin-to-cyrillic", "Salom") == "Салом"


def test_cli_clean_dataset():
    assert run_cli("clean-dataset", "  Салом!!!  ") == "Салом!"
