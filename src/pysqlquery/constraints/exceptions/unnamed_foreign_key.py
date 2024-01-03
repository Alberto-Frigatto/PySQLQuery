from abc import ABCMeta
from typing import Any
from .unnamed_constraint import UnnamedConstraintException


class UnnamedForeignKeyException(UnnamedConstraintException, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidRefTable(UnnamedForeignKeyException):
    MESSAGE = 'Invalid referencied table: {ref_table!r}'

    def __init__(self, ref_table: Any) -> None:
        super().__init__(self.MESSAGE.format(ref_table=ref_table))


class InvalidRefColumn(UnnamedForeignKeyException):
    MESSAGE = 'Invalid referencied column:  {ref_table!r}.{ref_column!r}'

    def __init__(self, ref_table: str, ref_column: Any) -> None:
        super().__init__(self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column))


class MissingColumnName(UnnamedForeignKeyException):
    MESSAGE = 'Missing column name in ForeignKey constraint for {ref_table}.{ref_column}'

    def __init__(self, ref_table: str, ref_column: str) -> None:
        super().__init__(self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column))


class InvalidOnDeleteClause(UnnamedForeignKeyException):
    MESSAGE = ("The given value in ForeignKey constraint for {ref_table}.{ref_column} is an invalid option for on_delete clause.\n"
               "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict', but {on_delete!r} was passed")

    def __init__(self, ref_table: str, ref_column: str, on_delete: Any) -> None:
        super().__init__(self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column, on_delete=on_delete))


class InvalidOnUpdateClause(UnnamedForeignKeyException):
    MESSAGE = ("The given value in ForeignKey constraint for {ref_table}.{ref_column} is an invalid option for on_update clause.\n"
               "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict', but {on_update!r} was passed")

    def __init__(self, ref_table: str, ref_column: str, on_update: Any) -> None:
        super().__init__(self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column, on_update=on_update))
