'''
Defines the base exception classes for SQL table.
'''

from abc import ABCMeta
from typing import Any


class TableException(Exception, metaclass=ABCMeta):
    '''
    Abstract base exception class for column-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidName(TableException):
    '''
    Exception raised for an invalid table's name.
    '''

    MESSAGE = 'The given value is an invalid table name: {name!r}'

    def __init__(self, name: Any) -> None:
        '''
        Parameters
        ----------
        name : Any
            The invalid table's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(name=name))


class InvalidConstraintList(TableException):
    '''
    Exception raised for an invalid constraint list.
    '''

    MESSAGE = 'The constraint list of {table} table is invalid, it must be a list[NamedConstraint]'

    def __init__(self, table: str) -> None:
        '''
        Parameters
        ----------
        table : str
            The table's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(table=table))


class InvalidNamedConstraint(TableException):
    '''
    Exception raised for an invalid named constraint.
    '''

    MESSAGE = (
        'The {name} constraint is invalid, it references a non-existent column in {table} table'
    )

    def __init__(self, table: str, constraint_name: str) -> None:
        '''
        Parameters
        ----------
        table : str
            The table's name.
        constraint_name : str
            The constraint's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(name=constraint_name, table=table))


class MultiplePrimaryKeyConstraints(TableException):
    '''
    Exception raised for when the table receive multiple named primary key constraints.
    '''

    MESSAGE = 'The {table} table have multiple primary key constraints'

    def __init__(self, table: str) -> None:
        '''
        Parameters
        ----------
        table : str
            The table's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(table=table))


class InvalidTestValue(TableException):
    '''
    Exception raised for an invalid test value.
    '''

    MESSAGE = 'The test parameter of {table} table must be bool, but {value!r} was passed'

    def __init__(self, table: str, value: Any) -> None:
        '''
        Parameters
        ----------
        table : str
            The table's name.
        value : Any
            The invalid test value.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(table=table, value=value))


class InvalidCreateIfNotExistsValue(TableException):
    '''
    Exception raised for an invalid create_if_not_exists value.
    '''

    MESSAGE = (
        'The create_if_not_exists parameter of {table} table must be bool, but {value!r} was passed'
    )

    def __init__(self, table: str, value: Any) -> None:
        '''
        Parameters
        ----------
        table : str
            The table's name.
        value : Any
            The invalid create_if_not_exists value.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(table=table, value=value))
