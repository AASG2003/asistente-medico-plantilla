"""Text normalization done in Python, so it behaves the same on every database."""

import unicodedata


def normalize_name(value: str) -> str:
    """Lowercase, strip accents and collapse whitespace: 'Dolor de  Cabéza' -> 'dolor de cabeza'."""
    decomposed = unicodedata.normalize("NFKD", value)
    without_accents = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(without_accents.lower().split())
