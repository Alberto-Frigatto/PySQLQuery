'''
Defines the base exception classes for decimal SQL type classes
'''

from abc import ABCMeta
from typing import Any
from .sql_type import SQLTypeException

class SQLDecimalTypeException(SQLTypeException, metaclass=ABCMeta):
    '''
    Abstract base exception class for decimal SQL type-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidPrecision(SQLTypeException):
    '''
    Exception raised for an invalid decimal SQL type precision.
    '''

    MESSAGE = 'The given precision of {type} type is invalid: {precision!r}'

    def __init__(self, type_name: str, precision: Any) -> None:
        '''
        Parameters
        ----------
        type_name : str
            The name of SQL type.
        precision : Any
            The precision of SQL type.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(type=type_name, precision=precision))
