'''
Defines the base exception classes for decimal SQL type classes
'''

from .base_type import SqlBaseTypeException

class SqlBaseDecimalTypeException(SqlBaseTypeException):
    '''
    Abstract base exception class for decimal SQL type-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidPrecision(SqlBaseTypeException):
    '''
    Exception raised for an invalid decimal SQL type precision.
    '''

    MESSAGE = 'A precisão para o tipo {type} é inválido'

    def __init__(self, type_name: str) -> None:
        '''
        Parameters
        ----------
        type_name : str
            The name of SQL type.

        Returns
        -------
        None
        '''

        super().__init__(self.MESSAGE.format(type=type_name))
