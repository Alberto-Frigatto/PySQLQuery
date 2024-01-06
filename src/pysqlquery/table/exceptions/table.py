from abc import ABCMeta
from typing import Any


class TableException(Exception, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidName(TableException):
    MESSAGE = 'The given value is an invalid table name: {name!r}'

    def __init__(self, name: Any) -> None:
        super().__init__(self.MESSAGE.format(name=name))


class InvalidConstraintList(TableException):
    MESSAGE = 'The constraint list of {table} table is invalid, it must be a list[NamedConstraint]'

    def __init__(self, table: str) -> None:
        super().__init__(self.MESSAGE.format(table=table))


class InvalidNamedConstraint(TableException):
    MESSAGE = 'The {name} constraint is invalid, it references a non-existent column in {table} table'

    def __init__(self, table: str, constraint_name: str) -> None:
        super().__init__(self.MESSAGE.format(name=constraint_name, table=table))


class MultiplePrimaryKeyConstraints(TableException):
    MESSAGE = 'The {table} table have multiple primary key constraints'

    def __init__(self, table: str) -> None:
        super().__init__(self.MESSAGE.format(table=table))


class InvalidTestValue(TableException):
    MESSAGE = 'The __test__ attibute of {table} table must be bool, but {value!r} was passed'

    def __init__(self, table: str, value: Any) -> None:
        super().__init__(self.MESSAGE.format(table=table, value=value))
