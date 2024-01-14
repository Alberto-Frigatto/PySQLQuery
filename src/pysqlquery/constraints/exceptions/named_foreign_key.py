'''
Defines the base exception classes for ForeignKeyConstraint class.
'''

from abc import ABCMeta
from typing import Any

from .multi_column_named_constraint import MultiColumnNamedConstraintException


class NamedForeignKeyException(MultiColumnNamedConstraintException, metaclass=ABCMeta):
    '''
    Abstract base exception class for ForeignKeyConstraint-related exceptions.
    '''


class InvalidRefTable(NamedForeignKeyException):
    '''
    Exception raised for an invalid referenced table name.
    '''

    MESSAGE = (
        'The given value in {constraint} constraint is an invalid referencied table: {ref_table!r}'
    )

    def __init__(self, constraint_name: str, ref_table: Any) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.
        ref_table : Any
            The invalid referenced table name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name, ref_table=ref_table))


class InvalidRefColumnType(NamedForeignKeyException):
    '''
    Exception raised for an invalid referenced column type.
    '''

    MESSAGE = (
        'The given value for the ref_column parameter in {constraint}'
        ' constraint must be a str or list[str], but a {type!r} was passed'
    )

    def __init__(self, constraint_name: str, ref_column: Any) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.
        ref_column : Any
            The invalid referenced column name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name, type=type(ref_column)))


class InvalidRefColumn(NamedForeignKeyException):
    '''
    Exception raised for an invalid referenced column name.
    '''

    MESSAGE = (
        'The given value in {constraint} constraint is'
        ' an invalid referencied column: {ref_column!r}'
    )

    def __init__(self, constraint_name: str, ref_column: Any) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.
        ref_column : Any
            The invalid referenced column name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name, ref_column=ref_column))


class InvalidRefColumnListLength(NamedForeignKeyException):
    '''
    Exception raised for an invalid referenced column list length.
    '''

    MESSAGE = (
        'The given referencied column list in {constraint} constraint'
        ' have an invalid length: {ref_length}\n'
        'The list must would have length {columns_length}'
    )

    def __init__(self, constraint_name: str, ref_length: Any, columns_length: int) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.
        ref_length : Any
            The invalid referenced column list length.
        columns_length : int
            The column list length.

        Returns
        -------
        None
        '''

        super().__init__(
            self.MESSAGE.format(
                constraint=constraint_name, ref_length=ref_length, columns_length=columns_length
            )
        )


class RefColumnMustBeList(NamedForeignKeyException):
    '''
    Exception raised for when referenced column must be list.
    '''

    MESSAGE = 'The ref_column parameter of {constraint} constraint must be a list'

    def __init__(self, constraint_name: str) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name))


class RefColumnMustBeStr(NamedForeignKeyException):
    '''
    Exception raised for when referenced column must be str.
    '''

    MESSAGE = 'The ref_column parameter of {constraint} constraint must be a str'

    def __init__(self, constraint_name: str) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name))


class InvalidOnDeleteClause(NamedForeignKeyException):
    '''
    Exception raised for an invalid on delete clause.
    '''

    MESSAGE = (
        "The given value in {constraint} constraint is"
        " an invalid option for on_delete clause.\n"
        "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict'"
        ", but {on_delete!r} was passed"
    )

    def __init__(self, constraint_name: str, on_delete: Any) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.
        on_delete : Any
            The invalid on delete clause.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name, on_delete=on_delete))


class InvalidOnUpdateClause(NamedForeignKeyException):
    '''
    Exception raised for an invalid on update clause.
    '''

    MESSAGE = (
        "The given value in {constraint} constraint is"
        " an invalid option for on_update clause.\n"
        "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict'"
        ", but {on_update!r} was passed"
    )

    def __init__(self, constraint_name: str, on_update: Any) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.
        on_update : Any
            The invalid on update clause.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name, on_update=on_update))
