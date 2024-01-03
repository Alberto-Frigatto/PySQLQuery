from abc import ABCMeta
from typing import Any
from .constraint import ConstraintException


class UnnamedConstraintException(ConstraintException, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidAddedColumnName(UnnamedConstraintException):
    MESSAGE = 'Added a invalid column name in ForeignKey constraint: {column!r}'

    def __init__(self, column: Any) -> None:
        super().__init__(self.MESSAGE.format(column=column))
