'''
Defines the base exception classes for SQL text type classes.
'''

from abc import ABCMeta
from typing import Any

from .sql_type import SQLTypeException


class SQLTextTypeException(SQLTypeException, metaclass=ABCMeta):
    '''
    Abstract base exception class for SQL text type-related exceptions.
    '''


class InvalidTypeLength(SQLTextTypeException):
    '''
    Exception raised for an invalid SQL type length.
    '''

    MESSAGE = 'The given length of {type} type is invalid: {length!r}'

    def __init__(self, type_name: str, length: Any) -> None:
        '''
        Parameters
        ----------
        type_name : str
            The name of SQL type.
        length : Any
            The length of SQL type.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(type=type_name, length=length))
