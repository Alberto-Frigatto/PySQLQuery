'''
Defines the Time class for constructing TIME SQL type.
'''

from datetime import datetime

from .base import SQLDateType


class Time(SQLDateType):
    '''
    Represents a TIME data type in SQL.

    This class inherits from `SQLDateType` and provides functionality
    specific to the TIME data type in `HH:MM:ss` pattern.
    '''

    _TYPE_NAME = 'time'

    def __init__(self) -> None:
        '''
        Examples
        --------
        >>> time_type = Date()
        >>> print(time_type)
        TIME
        '''

        TIME_PATTERN = '%H:%M:%S'
        super().__init__(self._TYPE_NAME, TIME_PATTERN)

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
            True if the value is valid for the TIME SQL type in `HH:MM:ss` pattern, False otherwise.

        Examples
        --------
        >>> time_type = Date()
        >>> time_type.validate_value('20:45:31')
        True
        >>> time_type.validate_value('20-45-31')
        False
        >>> time_type.validate_value('abc')
        False
        >>> time_type.validate_value(10)
        False
        '''

        try:
            datetime.strptime(value, super().pattern)
        except (TypeError, ValueError):
            return False

        return True
