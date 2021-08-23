"""Модуль, в котором создаются пользовательские классы исключений."""


class InputParameterVerificationError(Exception):
    """Исключение, возникающее в случае провала проверки входных параметров."""

    def __init__(
        self, message: str ="Входные параметры не прошли валидацию.",
    ) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"


class ResultVerificationError(Exception):
    """Исключение, возникающее в случае провала проверки выходных параметров."""

    def __init__(
        self, message: str ="Результат выполнения функции не прошёл валидацию.",
    ) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"
