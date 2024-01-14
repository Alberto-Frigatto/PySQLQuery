'''
Defines the base exception classes for ForeignKey class.
'''

from abc import ABCMeta
from typing import Any

from .unnamed_constraint import UnnamedConstraintException


class UnnamedForeignKeyException(UnnamedConstraintException, metaclass=ABCMeta):
    '''
    Abstract base exception class for ForeignKey-related exceptions.
    '''


class InvalidRefTable(UnnamedForeignKeyException):
    '''
    Exception raised for an invalid referenced table name.
    '''

    MESSAGE = 'Invalid referencied table: {ref_table!r}'

    def __init__(self, ref_table: Any) -> None:
        '''
        Parameters
        ----------
        ref_table : Any
            The invalid referenced table name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(ref_table=ref_table))


class InvalidRefColumn(UnnamedForeignKeyException):
    '''
    Exception raised for an invalid referenced column name.
    '''

    MESSAGE = 'Invalid referencied column:  {ref_table!r}.{ref_column!r}'

    def __init__(self, ref_table: str, ref_column: Any) -> None:
        '''
        Parameters
        ----------
        ref_table : str
            The referenced table name.
        ref_column : Any
            The invalid referenced column name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column))


class MissingColumnName(UnnamedForeignKeyException):
    '''
    Exception raised for missing column name.
    '''

    MESSAGE = 'Missing column name in ForeignKey constraint for {ref_table}.{ref_column}'

    def __init__(self, ref_table: str, ref_column: str) -> None:
        '''
        Parameters
        ----------
        ref_table : str
            The referenced table name.
        ref_column : str
            The referenced column name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column))


class InvalidOnDeleteClause(UnnamedForeignKeyException):
    '''
    Exception raised for an invalid on delete clause.
    '''

    MESSAGE = (
        "The given value in ForeignKey constraint for {ref_table}.{ref_column} is"
        " an invalid option for on_delete clause.\n"
        "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict'"
        ", but {on_delete!r} was passed"
    )

    def __init__(self, ref_table: str, ref_column: str, on_delete: Any) -> None:
        '''
        Parameters
        ----------
        ref_table : str
            The referenced table name.
        ref_column : str
            The referenced column name.
        on_delete : Any
            The invalid on delete clause.

        Returns
        -------
        None
        '''

        super().__init__(
            self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column, on_delete=on_delete)
        )


class InvalidOnUpdateClause(UnnamedForeignKeyException):
    '''
    Exception raised for an invalid on update clause.
    '''

    MESSAGE = (
        "The given value in ForeignKey constraint for {ref_table}.{ref_column} is"
        " an invalid option for on_update clause.\n"
        "It must be 'cascade', 'set null', 'set default', 'no action' or 'restrict'"
        ", but {on_update!r} was passed"
    )

    def __init__(self, ref_table: str, ref_column: str, on_update: Any) -> None:
        '''
        Parameters
        ----------
        ref_table : str
            The referenced table name.
        ref_column : str
            The referenced column name.
        on_update : Any
            The invalid on update clause.

        Returns
        -------
        None
        '''

        super().__init__(
            self.MESSAGE.format(ref_table=ref_table, ref_column=ref_column, on_update=on_update)
        )
