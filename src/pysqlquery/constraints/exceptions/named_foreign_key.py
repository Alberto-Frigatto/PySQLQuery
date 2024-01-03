from abc import ABCMeta
from typing import Any
from .multi_column_named_constraint import MultiColumnNamedConstraintException


class NamedForeignKeyException(MultiColumnNamedConstraintException, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidRefTable(NamedForeignKeyException):
    MESSAGE = 'The given value in {constraint} constraint is an invalid referencied table: {ref_table!r}'

    def __init__(self, constraint_name: str, ref_table: Any) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, ref_table=ref_table))


class InvalidRefColumnType(NamedForeignKeyException):
    MESSAGE = 'The given value for the ref_column parameter in {constraint} constraint must be a str or list[str], but a {type!r} was passed'

    def __init__(self, constraint_name: str, ref_column: Any) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, type=type(ref_column)))


class InvalidRefColumn(NamedForeignKeyException):
    MESSAGE = 'The given value in {constraint} constraint is an invalid referencied column: {ref_column!r}'

    def __init__(self, constraint_name: str, ref_column: Any) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, ref_column=ref_column))


class InvalidRefColumnListLength(NamedForeignKeyException):
    MESSAGE = ('The given referencied column list in {constraint} constraint have an invalid length: {ref_length}\n'
               'The list must would have length {columns_length}')

    def __init__(self, constraint_name: str, ref_length: Any, columns_length: int) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, ref_length=ref_length, columns_length=columns_length))


class RefColumnMustBeList(NamedForeignKeyException):
    MESSAGE = 'The ref_column parameter of {constraint} constraint must be a list'

    def __init__(self, constraint_name: str) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name))


class RefColumnMustBeStr(NamedForeignKeyException):
    MESSAGE = 'The ref_column parameter of {constraint} constraint must be a str'

    def __init__(self, constraint_name: str) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name))


class InvalidOnDeleteClause(NamedForeignKeyException):
    MESSAGE = ("The given value in {constraint} constraint is an invalid option for on_delete clause.\n"
               "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict', but {on_delete!r} was passed")

    def __init__(self, constraint_name: str, on_delete: Any) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, on_delete=on_delete))


class InvalidOnUpdateClause(NamedForeignKeyException):
    MESSAGE = ("The given value in {constraint} constraint is an invalid option for on_update clause.\n"
               "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict', but {on_update!r} was passed")

    def __init__(self, constraint_name: str, on_update: Any) -> None:
        super().__init__(self.MESSAGE.format(constraint=constraint_name, on_update=on_update))
