'''
Defines the base exception classes for SQL column.
'''

from abc import ABCMeta
from typing import Any


class ColumnException(Exception, metaclass=ABCMeta):
    '''
    Abstract base exception class for column-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidSQLType(ColumnException):
    '''
    Exception raised for an invalid SQL type.
    '''

    MESSAGE = 'Invalid SQL type for column: {data_type!r}'

    def __init__(self, data_type: Any) -> None:
        '''
        Parameters
        ----------
        data_type : Any
            The invalid SQL data type.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(data_type=data_type))


class InvalidForeignKey(ColumnException):
    '''
    Exception raised for an invalid ForeignKey.
    '''

    MESSAGE = (
        'Invalid foreign_key parameter, it must be a ForeignKey or None, but {value!r} was passed'
    )

    def __init__(self, value: Any) -> None:
        '''
        Parameters
        ----------
        value : Any
            The invalid foreign key.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(value=value))


class InvalidPrimaryKey(ColumnException):
    '''
    Exception raised for an invalid primary key value.
    '''

    MESSAGE = 'Invalid primary_key parameter: {value!r}'

    def __init__(self, value: Any) -> None:
        '''
        Parameters
        ----------
        value : Any
            The invalid primary key.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(value=value))


class InvalidAutoIncrement(ColumnException):
    '''
    Exception raised for an invalid auto increment value.
    '''

    MESSAGE = (
        "The given value is an invalid option for auto_increment.\n"
        "It must be 'mssql', 'mysql', 'sqlite' or 'postgree', but {value!r} was passed"
    )

    def __init__(self, value: Any) -> None:
        '''
        Parameters
        ----------
        value : Any
            The invalid auto increment.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(value=value))


class InvalidNullable(ColumnException):
    '''
    Exception raised for an invalid nullable value.
    '''

    MESSAGE = 'Invalid nullable parameter: {value!r}'

    def __init__(self, value: Any) -> None:
        '''
        Parameters
        ----------
        value : Any
            The invalid nullable value.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(value=value))


class InvalidUnique(ColumnException):
    '''
    Exception raised for an invalid unique value.
    '''

    MESSAGE = 'Invalid unique parameter: {value!r}'

    def __init__(self, value: Any) -> None:
        '''
        Parameters
        ----------
        value : Any
            The invalid unique value.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(value=value))


class InvalidDefaultValue(ColumnException):
    '''
    Exception raised for an invalid default value.
    '''

    MESSAGE = 'The given default value {value!r} isn\'t a valid {data_type} data'

    def __init__(self, data_type: str, value: Any) -> None:
        '''
        Parameters
        ----------
        value : Any
            The invalid default value.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(value=value, data_type=data_type))


class ColumnAlreadyHasNamedForeignKeyConstraint(ColumnException):
    '''
    Exception raised for when column already own named foreign key constraint.
    '''

    MESSAGE = 'The {column} column already has a named foreign key constraint'

    def __init__(self, column: str) -> None:
        '''
        Parameters
        ----------
        column : str
            The column's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(column=column))


class ColumnAlreadyHasNamedUniqueConstraint(ColumnException):
    '''
    Exception raised for when column already own named unique constraint.
    '''

    MESSAGE = 'The {column} column already has a named unique constraint'

    def __init__(self, column: str) -> None:
        '''
        Parameters
        ----------
        column : str
            The column's name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(column=column))
