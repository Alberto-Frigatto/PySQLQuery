'''
Defines the abstract base class for constructing date SQL type classes.
'''

from abc import ABCMeta
import re
from . import SQLType
from pysqlquery.types.exceptions.sql_date_type import InvalidDatePattern


class SQLDateType(SQLType, metaclass=ABCMeta):
    '''
    Abstract class for construct date SQL type classes.

    This class inherits from `SQLType` and provides the basic structures for construct
    concrete classes that represents date SQL types or another
    abstract classes for other kind of date SQL types.

    This class must be inherited by concrete or another abstract one.
    '''

    def __init__(self, sql_type_name: str, date_pattern: str) -> None:
        '''
        Parameters
        ----------
        sql_type_name : str
            The name of date SQL type.
        date_pattern : str
            The pattern of date SQL type.

        Returns
        -------
        None
        '''

        super().__init__(sql_type_name, length=None)

        self._validate_pattern(date_pattern)
        self._pattern = self._format_pattern(date_pattern)

    def _validate_pattern(self, pattern: str) -> None:
        if not self._is_pattern_valid(pattern):
            raise InvalidDatePattern(super().name)

    def _is_pattern_valid(self, pattern: str) -> bool:
        return isinstance(pattern, str) and len(pattern) and re.search(r'%\w', pattern)

    def _format_pattern(self, pattern: str) -> str:
        return pattern.strip()

    @property
    def pattern(self) -> int:
        return self._pattern
