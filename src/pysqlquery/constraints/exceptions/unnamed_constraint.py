'''
Defines the base exception classes for unnamed SQL constraint classes.
'''

from abc import ABCMeta
from typing import Any
from .constraint import ConstraintException


class UnnamedConstraintException(ConstraintException, metaclass=ABCMeta):
    '''
    Abstract base exception class for unnamed SQL constraint-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidAddedColumnName(UnnamedConstraintException):
    '''
    Exception raised for an invalid added column name.
    '''

    MESSAGE = 'Added a invalid column name in ForeignKey constraint: {column!r}'

    def __init__(self, column: Any) -> None:
        '''
        Parameters
        ----------
        column : Any
            The invalid column name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(column=column))
