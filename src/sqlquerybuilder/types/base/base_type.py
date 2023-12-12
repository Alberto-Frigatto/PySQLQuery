'''
Defines the abstract base class for constructing SQL type classes.
'''

from abc import ABCMeta, abstractmethod
from typing import Any
from sqlgen.types.exceptions.base_type import InvalidTypeName, InvalidTypeLength


class BaseType(metaclass=ABCMeta):
    '''
    Abstract class for construct SQL type classes.

    This class provides the basic structures for construct
    concrete classes that represents SQL types or another
    abstract classes for other kind of SQL types.

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

        super().__init__()

        self._validate_name(sql_type_name)
        self._name: str = self._format_type_name(sql_type_name)

        self._validate_length(length)
        self._length: int | None = length

    def _validate_name(self, type: str) -> None:
        if not self._is_name_valid(type):
            raise InvalidTypeName()

    def _is_name_valid(self, type: str) -> bool:
        return isinstance(type, str) and len(type)

    def _validate_length(self, length: int | None) -> None:
        if not self._is_length_valid(length):
            raise InvalidTypeLength(self._name)

    def _is_length_valid(self, length: int | None) -> bool:
        return length is None or (isinstance(length, int) and length > 0)

    def _format_type_name(self, type: str) -> str:
        return type.strip().upper()

    @abstractmethod
    def __str__(self) -> str:
        '''
        Returns
        -------
        str
            A string representation of the class instance in SQL format.
        '''

        pass

    @abstractmethod
    def validate_value(self, value: Any) -> bool:
        '''
        Parameters
        ----------
        value : Any
            The value to be validated.

        Returns
        -------
        bool
            True if the value is valid for the SQL type, False otherwise.
        '''

        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def length(self) -> int:
        return self._length
