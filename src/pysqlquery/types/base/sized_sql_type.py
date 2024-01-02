'''
Defines the abstract base class for constructing sized SQL type classes like text types and numeric types.
'''

from abc import ABCMeta
from ..exceptions.sized_sql_type import InvalidTypeLength
from .sql_type import SQLType


class SizedSQLType(SQLType, metaclass=ABCMeta):
    '''
    Abstract class for construct abstract sized SQL type classes.

    This class inherits from `SQLType` and provides the basic structures for construct
    abstract classes for kind of sized SQL types like text types and numeric types.

    This class must be inherited by abstract one.
    '''

    def __init__(self, sql_type_name: str, length: int | None) -> None:
        '''
        Parameters
        ----------
        sql_type_name : str
            The name of SQL type.
        length : int | None
            The length of SQL type.

        Returns
        -------
        None
        '''

        super().__init__(sql_type_name)

        self._validate_length(length)
        self._length: int | None = length

    def _validate_length(self, length: int | None) -> None:
        if not self._is_length_valid(length):
            raise InvalidTypeLength(super().name, length)

    def _is_length_valid(self, length: int | None) -> bool:
        return length is None or (isinstance(length, int) and length > 0)

    @property
    def length(self) -> int | None:
        return self._length
