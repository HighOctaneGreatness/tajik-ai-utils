CYRILLIC_TO_LATIN = {
    "А": "A", "а": "a",
    "Б": "B", "б": "b",
    "В": "V", "в": "v",
    "Г": "G", "г": "g",
    "Ғ": "Gh", "ғ": "gh",
    "Д": "D", "д": "d",
    "Е": "E", "е": "e",
    "Ё": "Yo", "ё": "yo",
    "Ж": "Zh", "ж": "zh",
    "З": "Z", "з": "z",
    "И": "I", "и": "i",
    "Ӣ": "I", "ӣ": "i",
    "Й": "Y", "й": "y",
    "К": "K", "к": "k",
    "Қ": "Q", "қ": "q",
    "Л": "L", "л": "l",
    "М": "M", "м": "m",
    "Н": "N", "н": "n",
    "О": "O", "о": "o",
    "П": "P", "п": "p",
    "Р": "R", "р": "r",
    "С": "S", "с": "s",
    "Т": "T", "т": "t",
    "У": "U", "у": "u",
    "Ӯ": "U", "ӯ": "u",
    "Ф": "F", "ф": "f",
    "Х": "Kh", "х": "kh",
    "Ҳ": "H", "ҳ": "h",
    "Ч": "Ch", "ч": "ch",
    "Ҷ": "J", "ҷ": "j",
    "Ш": "Sh", "ш": "sh",
    "Ъ": "'", "ъ": "'",
    "Э": "E", "э": "e",
    "Ю": "Yu", "ю": "yu",
    "Я": "Ya", "я": "ya",
}

LATIN_TO_CYRILLIC_MULTI = {
    "Gh": "Ғ", "gh": "ғ",
    "Zh": "Ж", "zh": "ж",
    "Yo": "Ё", "yo": "ё",
    "Kh": "Х", "kh": "х",
    "Ch": "Ч", "ch": "ч",
    "Sh": "Ш", "sh": "ш",
    "Yu": "Ю", "yu": "ю",
    "Ya": "Я", "ya": "я",
}

LATIN_TO_CYRILLIC_SINGLE = {
    "A": "А", "a": "а",
    "B": "Б", "b": "б",
    "V": "В", "v": "в",
    "G": "Г", "g": "г",
    "D": "Д", "d": "д",
    "E": "Е", "e": "е",
    "Z": "З", "z": "з",
    "I": "И", "i": "и",
    "Y": "Й", "y": "й",
    "K": "К", "k": "к",
    "Q": "Қ", "q": "қ",
    "L": "Л", "l": "л",
    "M": "М", "m": "м",
    "N": "Н", "n": "н",
    "O": "О", "o": "о",
    "P": "П", "p": "п",
    "R": "Р", "r": "р",
    "S": "С", "s": "с",
    "T": "Т", "t": "т",
    "U": "У", "u": "у",
    "F": "Ф", "f": "ф",
    "H": "Ҳ", "h": "ҳ",
    "J": "Ҷ", "j": "ҷ",
    "'": "ъ",
}


def cyrillic_to_latin_tajik(text: str) -> str:
    """Transliterate Tajik Cyrillic text to a simple Latin representation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return "".join(CYRILLIC_TO_LATIN.get(char, char) for char in text)


def latin_to_cyrillic_tajik(text: str) -> str:
    """Transliterate a simple Tajik Latin representation to Cyrillic."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = text

    for source, target in LATIN_TO_CYRILLIC_MULTI.items():
        result = result.replace(source, target)

    result = "".join(LATIN_TO_CYRILLIC_SINGLE.get(char, char) for char in result)

    return result
