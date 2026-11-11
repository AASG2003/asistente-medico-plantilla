"""
Reusable helpers for the prompts: they fill the templates of tracker/prompts/
with the parameters of extraction.json.
"""

import re
from pathlib import Path


PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def as_text(value) -> str:
    """Lists become "a, b" and dictionaries "a 1, b 2"; anything else, plain text."""
    if isinstance(value, list):
        return ", ".join(value)
    if isinstance(value, dict):
        return ", ".join(f"{key} {item}" for key, item in value.items())
    return str(value)


def fill_template(name: str, params: dict) -> str:
    """Replaces every {{name}} of a template in prompts/. A missing parameter is a KeyError."""
    template = (PROMPTS_DIR / name).read_text(encoding="utf-8").strip()

    def value_of(match):
        return as_text(params[match.group(1)])

    return re.sub(r"\{\{(\w+)\}\}", value_of, template)
