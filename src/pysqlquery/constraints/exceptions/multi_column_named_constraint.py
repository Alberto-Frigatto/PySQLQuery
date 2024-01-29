'''
Defines the base exception classes for multi column named SQL constraint classes.
'''

from abc import ABCMeta
from typing import Any

from .named_constraint import NamedConstraintException


class MultiColumnNamedConstraintException(NamedConstraintException, metaclass=ABCMeta):
    '''
    Abstract base exception class for multi column named SQL constraint-related exceptions.
    '''


class InvalidColumnType(MultiColumnNamedConstraintException):
    '''
    Exception raised for an invalid column type.
    '''

    MESSAGE = (
        'The given value for the column parameter in {constraint}'
        ' constraint must be a str or list[str], but a {type!r} was passed'
    )

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

        super().__init__(self.MESSAGE.format(constraint=constraint_name, type=type(column)))
