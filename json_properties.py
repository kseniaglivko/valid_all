"""Функция, выполняющая фалидацию json-файла."""

from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_json(file: dict) -> bool:
    """Валидация json-файла."""
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema",
        "type": "object",
        "examples": [{"key": 0}],
        "required": ["key"],
        "properties": {"key": {"type": "integer"}},
    }
    try:
        validate(file, schema)
    except ValidationError:
        return False
    return True
