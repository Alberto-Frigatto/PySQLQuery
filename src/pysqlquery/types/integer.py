'''
Defines the Integer class for constructing INTEGER SQL type.
'''

from .base import SQLIntType


class Integer(SQLIntType):
    '''
    Represents a INTEGER data type in SQL.

    This class inherits from `SQLIntType` and provides functionality
    specific to the INTEGER data type.
    '''

    _TYPE_NAME = 'integer'

    def __init__(self, length: int | None = None) -> None:
        '''
        Parameters
        ----------
        length : int | None
            The length of INTEGER type.

        Returns
        -------
        None

        Examples
        --------
        >>> int_type = Integer()
        >>> print(int_type)
        INTEGER

        >>> int_type = Integer(4)
        >>> print(int_type)
        INTEGER(4)
        '''

        super().__init__(self._TYPE_NAME, length)

    def __str__(self) -> str:
        rendered_value = super().name

        if super().length:
            rendered_value += f'({super().length})'

        return rendered_value

    def validate_value(self, value: int) -> bool:
        '''
        Parameters
        ----------
        value : int
            The value to be validated.

        Returns
        -------
        bool
            True if the value is valid for the INTEGER SQL type, False otherwise.

        Examples
        --------
        >>> int_type = Integer()
        >>> int_type.validate_value(10)
        True
        >>> int_type.validate_value(10000000000000)
        True
        >>> int_type.validate_value(15.45)
        False

        >>> int_type = Integer(2)
        >>> int_type.validate_value(10)
        True
        >>> int_type.validate_value(100)
        False
        >>> int_type.validate_value(1.5)
        False
        '''

        return isinstance(value, int) and (len(str(value)) <= super().length if super().length else True)
