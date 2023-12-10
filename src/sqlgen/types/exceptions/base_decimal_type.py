from .base_type import SqlBaseTypeException

class SqlBaseDecimalTypeException(SqlBaseTypeException):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidPrecision(SqlBaseTypeException):
    MESSAGE = 'A precisão para o tipo {type} é inválido'

    def __init__(self, type_name: str) -> None:
        super().__init__(self.MESSAGE.format(type=type_name))
