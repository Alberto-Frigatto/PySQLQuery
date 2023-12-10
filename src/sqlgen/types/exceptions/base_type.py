from abc import ABCMeta


class SqlBaseTypeException(Exception, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidTypeName(SqlBaseTypeException):
    MESSAGE = 'Nome de tipo inválido'

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class InvalidTypeLength(SqlBaseTypeException):
    MESSAGE = 'Tamanho do tipo {type} é inválido'

    def __init__(self, type_name: str) -> None:
        super().__init__(self.MESSAGE.format(type=type_name))


class InvalidValue(SqlBaseTypeException):
    MESSAGE = 'O valor para o campo {type} é inválido'

    def __init__(self, type_name: str) -> None:
        super().__init__(self.MESSAGE.format(type=type_name))