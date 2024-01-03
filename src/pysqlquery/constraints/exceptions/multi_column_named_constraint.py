from abc import ABCMeta
from typing import Any
from .named_constraint import NamedConstraintException


class MultiColumnNamedConstraintException(NamedConstraintException, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidColumnType(MultiColumnNamedConstraintException):
    MESSAGE = 'The given value for the column parameter in {constraint} constraint must be a str or list[str], but a {type!r} was passed'

    def __init__(self, constraint_name: str, column: Any) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, type=type(column)))
