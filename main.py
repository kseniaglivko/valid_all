"""
Модуль, в котором определяется проверямая декоратором функция, а также осуществляется ее запуск.
При запуске main.py из консоли необходимо указать путь до валидируемого json-файла.
"""

import sys
import json
from decorator import valid_all
from utils import process_json, output_validation, default_function


path_to_json = str(sys.argv[1])


@valid_all(
    precondition=process_json,
    postcondition=output_validation,
    on_fail_repeat_times=0,
    default_behavior=default_function,
)
def find_user_email(path_to_file: str) -> str:
    """Тестовая функция для демонстрации работы декоратора."""
    with open(path_to_file, "r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError as ex:
            raise ex
    output = str(data["email"])
    print(f"Email участника: {output}.")
    return output


if __name__ == "__main__":
    # Запускаем функцию на проверку.
    find_user_email(path_to_json)
