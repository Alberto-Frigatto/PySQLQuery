'''
Defines the base exception classes for named SQL constraint classes.
'''

from abc import ABCMeta
from typing import Any

from .constraint import ConstraintException


class NamedConstraintException(ConstraintException, metaclass=ABCMeta):
    '''
    Abstract base exception class for named SQL constraint-related exceptions.
    '''


class InvalidConstraintName(NamedConstraintException):
    '''
    Exception raised for an invalid constraint name.
    '''

    MESSAGE = 'The given value is an invalid constraint name: {name!r}'

    def __init__(self, name: Any) -> None:
        '''
        Parameters
        ----------
        name : Any
            The invalid constraint name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(name=name))


class InvalidColumnName(NamedConstraintException):
    '''
    Exception raised for an invalid column name.
    '''

    MESSAGE = 'The given value for {constraint} constraint is an invalid column name: {column!r}'

    def __init__(self, constraint_name: str, column: Any) -> None:
        '''
        Parameters
        ----------
        constraint_name : str
            The constraint's name.
        column : Any
            The invalid column name.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(constraint=constraint_name, column=column))
