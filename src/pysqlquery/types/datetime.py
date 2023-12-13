'''
Defines the Date class for constructing DATETIME SQL type.
'''

from .base import SQLDateType
from datetime import datetime


class DateTime(SQLDateType):
    '''
    Represents a DATETIME data type in SQL.

    This class inherits from `SQLDateType` and provides functionality
    specific to the DATETIME data type in `yyyy-mm-dd HH-MM-ss` pattern.
    '''

    _TYPE_NAME = 'datetime'

    def __init__(self) -> None:
        '''
        Examples
        --------
        >>> datetime_type = DateTime()
        >>> print(datetime_type)
        DATETIME
        '''

        DATE_PATTERN = '%Y-%m-%d %H:%M:%S'
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
            True if the value is valid for the DATETIME SQL type in `yyyy-mm-dd HH:MM:ss` pattern, False otherwise.

        Examples
        --------
        >>> datetime_type = DateTime()
        >>> datetime_type.validate_value('2005-02-27 12:45:10')
        True
        >>> datetime_type.validate_value('2005-02-27')
        False
        >>> datetime_type.validate_value('abc')
        False
        >>> datetime_type.validate_value(10)
        False
        '''

        try:
            datetime.strptime(value, super().pattern)
        except Exception:
            return False

        return True