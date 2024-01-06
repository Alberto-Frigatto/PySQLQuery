from abc import ABCMeta
from typing import Any


class ColumnException(Exception, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidSQLType(ColumnException):
    MESSAGE = 'Invalid SQL type for column: {data_type!r}'

    def __init__(self, data_type: Any) -> None:
        super().__init__(self.MESSAGE.format(data_type=data_type))


class InvalidForeignKey(ColumnException):
    MESSAGE = 'Invalid foreign_key parameter, it must be a ForeignKey or None, but {value!r} was passed'

    def __init__(self, value: Any) -> None:
        super().__init__(self.MESSAGE.format(value=value))


class InvalidPrimaryKey(ColumnException):
    MESSAGE = 'Invalid primary_key parameter: {value!r}'

    def __init__(self, value: Any) -> None:
        super().__init__(self.MESSAGE.format(value=value))


class InvalidAutoIncrement(ColumnException):
    MESSAGE = ("The given value is an invalid option for auto_increment.\n"
                "It must be 'mssql', 'mysql', 'sqlite' or 'postgree', but {value!r} was passed")

    def __init__(self, value: Any) -> None:
        super().__init__(self.MESSAGE.format(value=value))


class InvalidNullable(ColumnException):
    MESSAGE = 'Invalid nullable parameter: {value!r}'

    def __init__(self, value: Any) -> None:
        super().__init__(self.MESSAGE.format(value=value))


class InvalidUnique(ColumnException):
    MESSAGE = 'Invalid unique parameter: {value!r}'

    def __init__(self, value: Any) -> None:
        super().__init__(self.MESSAGE.format(value=value))


class InvalidDefaultValue(ColumnException):
    MESSAGE = 'The given default value {value!r} isn\'t a valid {data_type} data'

    def __init__(self, data_type: str, value: Any) -> None:
        super().__init__(self.MESSAGE.format(value=value, data_type=data_type))


class ColumnAlreadyHasNamedForeignKeyConstraint(ColumnException):
    MESSAGE = 'The column already has a named foreign key constraint'

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class ColumnAlreadyHasNamedUniqueConstraint(ColumnException):
    MESSAGE = 'The column already has a named unique constraint'

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)
