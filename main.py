"""
Модуль, в котором определяется проверямая декоратором функция, а также осуществляется ее запуск.
При запуске main.py из консоли необходимо указать путь до валидируемого json-файла.
"""

import sys
from decorator import valid_all
from utils import process_json, output_validation, default_function


path_to_json = str(sys.argv[1])


@valid_all(
    precondition = process_json,
    postcondition = output_validation,
    on_fail_repeat_times = 2,
    default_behavior = default_function)
def find_user_email(json_file: str) -> str:
    """Тестовая функция для демонстрации работы декоратора."""
    output = "Email участника " + str(json_file["name"]) + " : " + str(json_file["email"]) + "."
    return output


if __name__ == "__main__":
    # Запускаем функцию на проверку.
    find_user_email(path_to_json)
