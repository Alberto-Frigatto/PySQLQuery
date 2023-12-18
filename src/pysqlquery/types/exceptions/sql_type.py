'''
Defines the base exception classes for SQL type classes
'''

from abc import ABCMeta


class SQLTypeException(Exception, metaclass=ABCMeta):
    '''
    Abstract base exception class for SQL type-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidTypeName(SQLTypeException):
    '''
    Exception raised for an invalid SQL type name.
    '''

    MESSAGE = 'The given value is an invalid SQL type name: {name!r}'

    def __init__(self, name: str) -> None:
        super().__init__(self.MESSAGE.format(name=name))
