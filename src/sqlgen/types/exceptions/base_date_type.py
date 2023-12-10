from .base_type import SqlBaseTypeException

class SqlBaseDateTypeException(SqlBaseTypeException):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidDatePattern(SqlBaseTypeException):
    MESSAGE = 'O padrão para o tipo {type} é inválido'

    def __init__(self, type_name: str) -> None:
        super().__init__(self.MESSAGE.format(type=type_name))
