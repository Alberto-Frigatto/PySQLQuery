from abc import ABCMeta, abstractmethod
from typing import Any
from sqlgen.types.exceptions.base_type import InvalidTypeName, InvalidTypeLength


class BaseType(metaclass=ABCMeta):
    def __init__(self, sql_type_name: str, length: int | None) -> None:
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
        pass

    @abstractmethod
    def validate_value(self, value: Any) -> bool:
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def length(self) -> int:
        return self._length
