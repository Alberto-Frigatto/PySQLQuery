from abc import ABCMeta
from .sql_type import SQLTypeException


class SizedSQLTypeException(SQLTypeException, metaclass=ABCMeta):
    '''
    Abstract base exception class for sized SQL type-related exceptions.
    '''

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidTypeLength(SizedSQLTypeException):
    '''
    Exception raised for an invalid SQL type length.
    '''

    MESSAGE = 'Tamanho do tipo {type} é inválido'

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
