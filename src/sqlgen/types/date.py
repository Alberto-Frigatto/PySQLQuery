'''
Defines the Date class for constructing DATE SQL type.
'''

from .base import BaseDateType
from datetime import datetime


class Date(BaseDateType):
    '''
    Represents a DATE data type in SQL.

    This class inherits from `BaseDateType` and provides functionality
    specific to the DATE data type in `yyyy-mm-dd` pattern.
    '''

    _TYPE_NAME = 'date'

    def __init__(self) -> None:
        '''
        Examples
        --------
        >>> date_type = Date()
        >>> print(date_type)
        DATE
        '''

        DATE_PATTERN = '%Y-%m-%d'
        super().__init__(self._TYPE_NAME, DATE_PATTERN)

    def __str__(self) -> str:
        rendered_value = super().name

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
            True if the value is valid for the DATE SQL type in `yyyy-mm-dd` pattern, False otherwise.

        Examples
        --------
        >>> date_type = Date()
        >>> date_type.validate_value('2005-02-27')
        True
        >>> date_type.validate_value('27-02-2005')
        False
        >>> date_type.validate_value('abc')
        False
        >>> date_type.validate_value(10)
        False
        '''

        try:
            datetime.strptime(value, super().pattern)
        except Exception:
            return False

        return True