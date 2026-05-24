import re

from models.element import ElementName


ELEMENT_KEYWORDS: dict[ElementName, set[str]] = {
    "earth": {
        "earth",
        "rock",
        "stone",
        "soil",
        "sand",
        "mountain",
        "tree",
        "forest",
        "leaf",
        "wood",
    },
    "water": {
        "water",
        "rain",
        "river",
        "sea",
        "ocean",
        "ice",
        "snow",
        "fish",
        "wave",
    },
    "wind": {
        "wind",
        "air",
        "sky",
        "cloud",
        "storm",
        "bird",
        "fly",
        "breeze",
    },
    "fire": {
        "fire",
        "flame",
        "heat",
        "sun",
        "lava",
        "burn",
        "ember",
        "smoke",
    },
    "light": {
        "light",
        "shine",
        "star",
        "holy",
        "angel",
        "bright",
        "day",
        "sunrise",
    },
    "dark": {
        "dark",
        "shadow",
        "night",
        "moon",
        "ghost",
        "void",
        "death",
        "black",
    },
}

ELEMENTS: tuple[ElementName, ...] = ("earth", "water", "wind", "fire", "light", "dark")


def _tokenize(word: str) -> list[str]:
    return [token for token in re.split(r"[^a-z]+", word.lower().strip()) if token]


def classify_element(word: str) -> ElementName:
    clean_word = word.strip().lower()
    if not clean_word:
        raise ValueError("word is required")

    tokens = _tokenize(clean_word)
    for element, keywords in ELEMENT_KEYWORDS.items():
        if clean_word in keywords or any(token in keywords for token in tokens):
            return element

    fallback_index = sum(ord(character) for character in clean_word) % len(ELEMENTS)
    return ELEMENTS[fallback_index]