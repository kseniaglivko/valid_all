"""
Модуль, в котором разработаны функции для валидации параметров, которые будут применяться в декораторе,
а также функция 'default_function'.
"""

import json
import jsonschema
import re
from exceptions import InputParameterVerificationError, ResultVerificationError


def process_json(path_to_file: str) -> None:
    """
    Функция, считывающая данные из json-файла и передающая их на обработку в функцию 'data_validation'.
    Также функция валидирует сам формат json-файла.
    """
    with open(path_to_file, "r") as file:
        try:
            data = json.load(file)
            input_validation(data)
        except json.decoder.JSONDecodeError:
            raise InputParameterVerificationError


def input_validation(data: dict) -> bool:
    """
    Функция, валидирующая полученные из функции 'process_json' данные согласно заданной схеме.
    Проверяются типы данных, строки по регулярному выражению ("pattern"),
    наличие передаваемого значения в списке возможных значений.
    """
    root_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://example.com/product.schema.json",
        "type": "object",
        "title": "Информация об участнике",
        "description": "Данные участника игры.",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "mobile_number": {"type": "string", "pattern": "^(8|\+7|7)(9)([0-9]{9}$)$"},
            "race": {
                "type": "string",
                "enum": ["эльф", "маг", "орк", "гном", "человек"],
            },
            "power": {
                "type": "string",
                "enum": [
                    "ночное зрение",
                    "регенерация",
                    "берсерк",
                    "магия земли",
                    "прокрастинация",
                ],
            },
        },
    }

    try:
        jsonschema.validate(data, root_schema)
    except jsonschema.ValidationError:
        raise InputParameterVerificationError
    else:
        print("Входные параметры прошли валидацию!")
        return True


def output_validation(output: str) -> bool:
    """Функция валидации возвращаемого результата по регулярному выражению."""
    pattern = "^([a-zA-Z0-9_.-]+)(@)([a-z]+)([.])([a-z]{2,})$"
    result = re.fullmatch(pattern, output)
    if result:
        print("Результат выполнения функции прошел валидацию!")
        return True
    else:
        raise ResultVerificationError


def default_function():
    print("¯\_(ツ)_/¯\nПохоже, требуемую информацию не получить. Удачи в другой раз!")
