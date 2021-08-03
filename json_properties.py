"""Модуль, в котором определяется используемая json-схема."""

# На настоящий момент проверки по регулярным варыжаениям определены в паттернах.
# В дальнейшем они будут перенесены в валидотор.

# import re


# def validate_regex(arg: str) -> bool:
#    regex = re.compile("^[a-zA-Z0-9]+$")
#    return bool(regex.match(arg))


root_schema = {
    "type": "object",
    "title": "Информация об участнике",
    "properties": {
        "name": {
            "type": "string"
        },
        #        "password": {
        #            "type": "string",
        #            "format": "password",
        #            "pattern": "(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{6,}"
        #        },
        "email": {
            "type": "number",
            "format": "email",
            "pattern": "([a-zA-Z0-9_.-]+)(@)([a-z]+)([.])([a-z]{2,})"
        },
        "mobile_number": {
            "type": "number",
            "pattern": "(8|\+7|7)(9)([0-9]{9}$)"
        },
        "race": {
            "type": "string",
            "enum": ["эльф", "маг", "орк", "гном", "человек"]
        },
        "power": {
            "type": "string",
            "enum": ["ночное зрение", "регенерация", "берсерк", "магия земли", "прокрастинация"]
        }
    }
}
