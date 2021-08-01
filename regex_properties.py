"""Функция, выполняющая валидацию строки по регулярному выражению."""

import re


def validate_regex(arg: str) -> bool:
    regex = re.compile("^[a-zA-Z0-9]+$")
    return bool(regex.match(arg))
