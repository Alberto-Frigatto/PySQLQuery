'''
Defines the base exception classes for SQL constraint classes.
'''

from abc import ABCMeta


class ConstraintException(Exception, metaclass=ABCMeta):
    '''
    Abstract base exception class for SQL constraint-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)
