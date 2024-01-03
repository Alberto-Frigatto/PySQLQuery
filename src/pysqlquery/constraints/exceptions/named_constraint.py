from abc import ABCMeta
from typing import Any
from .constraint import ConstraintException


class NamedConstraintException(ConstraintException, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidConstraintName(NamedConstraintException):
    MESSAGE = 'The given value is an invalid constraint name: {name!r}'

    def __init__(self, name: Any) -> None:
        super().__init__(self.MESSAGE.format(name=name))


class InvalidColumnName(NamedConstraintException):
    MESSAGE = 'The given value for {constraint} constraint is an invalid column name: {column!r}'

    def __init__(self, constraint_name: str, column: Any) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, column=column))
