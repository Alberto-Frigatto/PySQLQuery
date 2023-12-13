'''
Defines the String class for constructing VARCHAR SQL type.
'''

from .base import SQLType


class String(SQLType):
    '''
    Represents a VARCHAR data type in SQL.

    This class inherits from `SQLType` and provides functionality
    specific to the VARCHAR data type.
    '''

    _TYPE_NAME = 'varchar'

    def __init__(self, length: int | None = None) -> None:
        '''
        Parameters
        ----------
        length : int | None
            The length of VARCHAR type

        Returns
        -------
        None

        Examples
        --------
        >>> str_type = String()
        >>> print(str_type)
        VARCHAR

        >>> str_type = String(50)
        >>> print(str_type)
        VARCHAR(50)
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
            True if the value is valid for the VARCHAR SQL type, False otherwise.

        Examples
        --------
        >>> str_type = String()
        >>> str_type.validate_value('abc')
        True
        >>> str_type.validate_value('abcdefghijklmnopqrstuvwxyz')
        True
        >>> str_type.validate_value(10)
        False

        >>> str_type = String(4)
        >>> str_type.validate_value('ab')
        True
        >>> str_type.validate_value('abcd')
        True
        >>> str_type.validate_value('abcde')
        False
        '''

        return isinstance(value, str) and (len(value) <= super().length if super().length else True)
