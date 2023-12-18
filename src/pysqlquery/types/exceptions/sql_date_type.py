'''
Defines the base exception classes for date SQL type classes
'''

from abc import ABCMeta
from .sql_type import SQLTypeException

class SQLDateTypeException(SQLTypeException, metaclass=ABCMeta):
    '''
    Abstract base exception class for date SQL type-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidDatePattern(SQLTypeException):
    '''
    Exception raised for an invalid date SQL type pattern.
    '''

    MESSAGE = 'The given date pattern for the {type} type is invalid: {pattern!r}'

    def __init__(self, type_name: str, date_pattern: str) -> None:
        '''
        Parameters
        ----------
        type_name : str
            The name of SQL type.
        pattern : str
            The date pattern of date SQL type.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(type=type_name, pattern=date_pattern))
