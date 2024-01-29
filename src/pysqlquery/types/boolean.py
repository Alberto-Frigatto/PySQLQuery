'''
Defines the Boolean class for constructing BOOLEAN SQL type.
'''

from .base import SQLIntType


class Boolean(SQLIntType):
    '''
    Represents a BOOLEAN data type in SQL.

    This class inherits from `SQLIntType` and provides functionality
    specific to the BOOLEAN data type.
    '''

    _TYPE_NAME = 'boolean'

    def __init__(self) -> None:
        '''
        Examples
        --------
        >>> boolean_type = Boolean()
        >>> print(boolean_type)
        BOOLEAN
        '''

        super().__init__(self._TYPE_NAME, 1)

    def __str__(self) -> str:
        rendered_value = super().name

        return rendered_value

    def validate_value(self, value: bool) -> bool:
        '''
        Parameters
        ----------
        value : bool
            The value to be validated.

        Returns
        -------
        bool
            True if the value is valid for the BOOLEAN SQL type, False otherwise.

        Examples
        --------
        >>> boolean_type = Boolean()
        >>> boolean_type.validate_value(True)
        True
        >>> boolean_type.validate_value(False)
        True
        >>> boolean_type.validate_value(15.45)
        False
        >>> boolean_type.validate_value('abc')
        False
        '''

        return isinstance(value, bool)
