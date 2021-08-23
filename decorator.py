"""Модуль, в котором создается декоратор для валидации входных и выходных параметров функции."""


from typing import Any, Callable
from time import sleep
from exceptions import ResultVerificationError


def valid_all(
    precondition: Callable,
    postcondition: Callable,
    on_fail_repeat_times: int = 1,
    default_behavior: Callable = None,
) -> Callable:
    """
    Валидатор выходных и выходных параметров функции.

    Args;
        В качестве аргумента precondition должна функция, отвечающая за валидацию входного файла и входных параметров.
        В качестве аргумента postcondition должна передаваться функция, отвечающая за валидацию выходных параметров.
    """
    def outer_wrapper(function: Callable) -> Any:
        def inner_wrapper(*args: Any, **kwargs: Any) -> Any:
            print("Приступаем к валидации входных параметров.")
            sleep(1)
            precondition(*args, **kwargs)
            if precondition:
                print("Приступаем к проверке результата выполнения функции.")
                sleep(1.5)
                function_output = function(*args, **kwargs)
                if on_fail_repeat_times < 0:
                    while True:
                        try:
                            postcondition(function_output)
                            print("Функция прошла валидацию.")
                            break
                        except ResultVerificationError:
                            raise ResultVerificationError
                if on_fail_repeat_times == 0:
                    try:
                        postcondition(function_output)
                    except ResultVerificationError:
                        print("Функция не прошла валидацию.")
                        if default_behavior is not None:
                            default_behavior()
                            quit()
                        raise ResultVerificationError
                else:
                    for attempt in range(1, on_fail_repeat_times + 1):
                        print(f"Повторная проверка валидации результата № {attempt}.")
                        sleep(1.5)
                        try:
                            postcondition(function_output)
                        except ResultVerificationError as ex:
                            if (
                                default_behavior is not None
                                and attempt == on_fail_repeat_times
                            ):
                                default_behavior()
                                quit()
                            if (
                                default_behavior is None
                                and attempt == on_fail_repeat_times
                            ):
                                raise ex

        return inner_wrapper

    return outer_wrapper
