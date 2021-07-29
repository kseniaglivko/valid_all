"""Модуль, в котором создаются пользовательские классы исключений."""


class InputParameterVerificationError(Exception):
    """Исключение, возникающее в случае провала проверки входных параметров."""

    def __init__(
        self,
        input_value,
        message="Данный параметр не прошел валидацию. Проверьте входные параметры.",
    ):
        self.input_value = input_value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.input_value}: {self.message}"


class ResultVerificationError(Exception):
    """Исключение, возникающее в случае провала проверки выходных параметров."""

    def __init__(
        self,
        output_value,
        message="Данный результат выполнения функции не прошёл валидацию.",
    ):
        self.output_value = output_value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.output_value} - {self.message}"
