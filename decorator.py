"""Модуль, в котором создается декораторы, для валидации входных и выходных параметров функции, а также типов данных
ввода и вывода."""

from exceptions import InputParameterVerificationError, ResultVerificationError


# Примерная структура:
# 1. Валидация json = V
# 2. Валидация регулярных выражений = V
# 3. Валидатор типов - начат ниже.
# Необходимо реализовать функцию, которая бы извлекала данные для этой функции.
def validate_type(type_):
    """Функция проверяет входные или выходные данные на соответсвие требуемому типу."""

    def predicate(arg):
        return isinstance(arg, type_)

    return predicate


# Этот декоратор должен обрабатывать входные данные.
def input_validator(predicate, on_fail_repeat_times=1, default_behavior=None):
    """
    Валидатор входных данных. В качестве аргумента (predicate) должна передаваться одна из валидирующих функций,
    выбираемых исходя из требуемого типа входных данных.
    Через нее в valid_all передается инофрмация о валидности входных данных для дальнейшей обработки.
    """

    def wrapper(function):
        def inner(*args):
            if not predicate(*args):
                raise InputParameterVerificationError
            return function(*args)

        return inner

    return wrapper


# Этот декоратор должен обрабатывать результат функции.
def output_validator(predicate, on_fail_repeat_times=1, default_behavior=None):
    """
    Валидатор выходных данных. В качестве аргумента (predicate) должна передаваться одна из валидирующих функций,
    выбираемых исходя из требуемого типа входных данных.
    Через нее в valid_all передается инофрмация о валидности выходных данных для дальнейшей обработки.
    """

    def wrapper(function):
        def inner(*args):
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


@input_validator
@output_validator(predicate, on_fail_repeat_times=1, default_behavior=None)
def valid_all(function):
    """Финальный декоратор, через применение которого будет реализовываться проверка требуемой функции."""
    pass


def default_behaviour():
    print("¯\_(ツ)_/¯\nВероятно, этот нехороший человек наврал о своих способностях!")

