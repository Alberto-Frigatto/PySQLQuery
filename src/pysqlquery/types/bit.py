'''
Defines the Bit class for constructing BIT SQL type.
'''

from .base import SQLIntType


class Bit(SQLIntType):
    '''
    Represents a BIT data type in SQL.

    This class inherits from `SQLIntType` and provides functionality
    specific to the BIT data type.
    '''

    _TYPE_NAME = 'bit'

    def __init__(self) -> None:
        '''
        Examples
        --------
        >>> bit_type = Bit()
        >>> print(bit_type)
        BIT
        '''

        super().__init__(self._TYPE_NAME, 1)

    def __str__(self) -> str:
        rendered_value = super().name

        return rendered_value

    def validate_value(self, value: bool | int) -> bool:
        '''
        Parameters
        ----------
        value : bool
            The value to be validated.

        Returns
        -------
        bool
            True if the value is valid for the BIT SQL type, False otherwise.

        Examples
        --------
        >>> bit_type = Bit()
        >>> bit_type.validate_value(True)
        True
        >>> bit_type.validate_value(False)
        True
        >>> bit_type.validate_value(1)
        True
        >>> bit_type.validate_value(0)
        True
        >>> bit_type.validate_value(15.45)
        False
        >>> bit_type.validate_value('abc')
        False
        '''

        return isinstance(value, bool) or (isinstance(value, int) and value in (0, 1))
