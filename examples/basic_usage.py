from tajik_ai_utils import (
    clean_for_llm_dataset,
    cyrillic_to_latin_tajik,
    is_probably_tajik_text,
    latin_to_cyrillic_tajik,
    normalize_tajik_text,
)


text = "  Салом    дунё!!!  Ин   як   матни   тоҷикӣ аст.  "

print("Original:", text)
print("Normalized:", normalize_tajik_text(text))
print("Dataset clean:", clean_for_llm_dataset(text))
print("Is probably Tajik:", is_probably_tajik_text(text))
print("Cyrillic to Latin:", cyrillic_to_latin_tajik("Салом Тоҷикистон"))
print("Latin to Cyrillic:", latin_to_cyrillic_tajik("Salom Tojikiston"))
