'''
Defines the Char class for constructing CHAR SQL type.
'''

from .base import SQLType


class Char(SQLType):
    '''
    Represents a CHAR data type in SQL.

    This class inherits from `SQLType` and provides functionality
    specific to the CHAR data type.
    '''

    _TYPE_NAME = 'char'

    def __init__(self, length: int | None = None) -> None:
        '''
        Parameters
        ----------
        length : int | None
            The length of CHAR type (if it isn't passed, will be 1)

        Returns
        -------
        None

        Examples
        --------
        >>> char_type = Char()
        >>> print(char_type)
        CHAR

        >>> char_type = Char(5)
        >>> print(char_type)
        CHAR(5)
        '''

        super().__init__(self._TYPE_NAME, length)

    def __str__(self) -> str:
        rendered_value = super().name

        if super().length:
            rendered_value += f'({super().length})'

        return rendered_value

    def validate_value(self, value: str) -> bool:
        '''
        Parameters
        ----------
        value : str
            The value to be validated.

        Returns
        -------
        bool
            True if the value is valid for the CHAR SQL type, False otherwise.

        Examples
        --------
        >>> char_type = Char()
        >>> char_type.validate_value('a')
        True
        >>> char_type.validate_value('ab')
        False

        >>> char_type = Char(3)
        >>> char_type.validate_value('abc')
        True
        >>> char_type.validate_value('abcd')
        False
        >>> char_type.validate_value(12)
        False
        '''

        return isinstance(value, str) and len(value) <= (super().length if super().length else 1)
