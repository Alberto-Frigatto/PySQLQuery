'''
Defines the base exception class for numeric SQL type classes.
'''

from abc import ABCMeta
from typing import Any

from .sql_type import SQLTypeException


class SQLNumTypeException(SQLTypeException, metaclass=ABCMeta):
    '''
    Abstract base exception class for numeric SQL type-related exceptions.
    '''


class InvalidPrecision(SQLNumTypeException):
    '''
    Exception raised for an invalid precision.
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
