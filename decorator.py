"""Модуль, в котором создается декоратор для валидации входных и выходных параметров функции,"""


from typing import Any, Callable


def valid_all(
    precondition: Callable,
    postcondition: Callable,
    on_fail_repeat_times: int = 1,
    default_behavior: Callable = None,
) -> Callable:
    """
    Валидатор выходных и выходных параметров функции.
    В качестве аргумента precondition должна функция, отвечающая за валидацию входного файла и входных параметров.
    В качестве аргумента postcondition должна передаваться функция, отвечающая за валидацию выходных параметров.
    """

    def outer_wrapper(function: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not predicate(*args):
                if on_fail_repeat_times != 0:
                    if on_fail_repeat_times > 0:
                        while on_fail_repeat_times > 0:
                            for _ in range(on_fail_repeat_times):
                                function(*args)
                    if on_fail_repeat_times < 0:
                        while True:
                            function(*args)
                if default_behavior is not None:
                    default_behaviour()
                raise ResultVerificationError
            return function(*args)

        return inner

    return wrapper
