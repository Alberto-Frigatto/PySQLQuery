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

    MESSAGE = 'Nome de tipo inválido'

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class InvalidTypeLength(SQLTypeException):
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


class InvalidValue(SQLTypeException):
    '''
    Exception raised for an invalid SQL type value.
    '''

    MESSAGE = 'O valor para o campo {type} é inválido'

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