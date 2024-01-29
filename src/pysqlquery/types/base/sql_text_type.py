'''
Defines the abstract base class for constructing text SQL type classes.
'''

from abc import ABCMeta

from ..exceptions.sql_text_type import InvalidTypeLength
from .sql_type import SQLType


class SQLTextType(SQLType, metaclass=ABCMeta):
    '''
    Abstract class for construct text SQL type classes.

    This class inherits from `SQLType` and provides the basic structures for construct
    concrete classes that represents text SQL types or another
    abstract classes for other kind of text SQL types.

    This class must be inherited by concrete or another abstract one.
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
