"""Модуль, в котором создаются пользовательские классы исключений."""


class InputParameterVerificationError(Exception):
    """Исключение, возникающее в случае провала проверки входных параметров."""

    def __init__(
        self, message="Входные параметры не прошли валидацию.",
    ):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class ResultVerificationError(Exception):
    """Исключение, возникающее в случае провала проверки выходных параметров."""

    def __init__(
        self, message="Результат выполнения функции не прошёл валидацию.",
    ):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
