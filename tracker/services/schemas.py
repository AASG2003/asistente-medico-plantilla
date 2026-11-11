"""
What Gemma must answer. The same models shape Gemma's JSON (they are sent as
its response schema) and validate it before anything is saved. They do not
create database tables.
"""

import json
from pathlib import Path

# --- Example -------------------------------------------------------------------
# class SchemaExample(BaseModel):
#     name: str = Field(min_length=1, max_length=100)        # required text with limits
#     kind: Literal["first", "second"]                       # only these values
#     amount: float | None = Field(default=None, ge=0)       # optional, not negative
#     tags: list[str] = []                                   # a list, empty by default
#
#     @field_validator("name", mode="before")                # runs before validating
#     @classmethod
#     def clean_name(cls, value):
#         return value.strip() if value else value
#
#
# example = SchemaExample.model_validate_json('{"name": "cafe", "kind": "first"}')  # ValidationError if wrong
# -------------------------------------------------------------------------------

PARAMS_FILE = Path(__file__).resolve().parent.parent / "prompts" / "extraction.json"
PROMPT_PARAMS = json.loads(PARAMS_FILE.read_text(encoding="utf-8"))
MAX_QUESTIONS = PROMPT_PARAMS["max_questions"]
INTENSITY_MAX = PROMPT_PARAMS["intensity_max"]
MAX_DAYS_BACK = PROMPT_PARAMS["max_days_back"]
