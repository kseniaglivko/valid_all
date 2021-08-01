"""
Программа для запуска проверки функции с помощью валидатора valid_all.

Необходимо запустить данный файл из консоли в формате: "python3 main.py <имя_файла>".

Программа уведомит о результатах проверки и выполнит требуемую функцию.
"""

import sys
import os


path_to_function = str(sys.argv[1])


def run_validation_checks(path_to_file: str) -> None:
    """
    Функция принимает путь до файла и добаляет импорт и запуск валдатора в указанный файл.
    Таким образом осуществлется подготовка к проверке валидатором требуемой функции.
    """

    with open(path_to_file, "r") as f:
        data = f.read()
    with open(path_to_file, "w") as f:
        f.writelines(["from decorator import valid_all\n\n"])
        f.writelines(["@valid_all\n"])
        f.writelines(data)


if __name__ == "__main__":
    # Давляем валидатор для проверки в файл и запускаем требуемую функцию.
    run_validation_checks(path_to_function)
    os.system(f"python3 {path_to_function}")
