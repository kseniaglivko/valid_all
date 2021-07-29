"""Модуль, в котором создается декораторы, для валидации входных и выходных параметров функции, а также типов данных
ввода и вывода."""

from exceptions import InputParameterVerificationError, ResultVerificationError


# Необходимо реализовать функцию, которая бы извлекала данные для этого декоратора.
def type_validator(type_):
    def predicate(arg):
        return isinstance(arg, type_)
    return predicate


# Этот декоратор должен обрабатывать входные данные.
def input_validator(predicate):
    def wrapper(function):
        def inner(arg):
            if not predicate(arg):
                raise InputParameterVerificationError
            return function(arg)
        return inner
    return wrapper


# Этот декоратор должен обрабатывать результат функции. Надо подумать, как их связать воедино.
def output_validator(predicate, on_fail_repeat_times=1, default_behavior=None):
    def wrapper(function):
        def inner(arg):
            if not predicate(arg):
                if on_fail_repeat_times != 0:
                    if on_fail_repeat_times > 0:
                        while on_fail_repeat_times > 0:
                            behaviour = default_behavior
                            counter = on_fail_repeat_times - 1
                            output_validator(predicate, counter, default_behavior=behaviour)
                            # А как проверяемая функция будет меняться?
                    if on_fail_repeat_times < 0:
                        behaviour = default_behavior
                        value = on_fail_repeat_times
                        output_validator(predicate, on_fail_repeat_times=value, default_behavior=behaviour)
                if default_behavior is not None:
                    default_behaviour()
                raise ResultVerificationError
            return function(arg)
        return inner
    return wrapper


def default_behaviour():
    print("¯\_(ツ)_/¯\nВсе плохо, переделывай!")

