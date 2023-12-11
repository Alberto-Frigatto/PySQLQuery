from typing import Any
from . import BaseType
from sqlgen.types.exceptions.base_decimal_type import InvalidPrecision


class BaseDecimalType(BaseType):
    def __init__(self, sql_type_name: str, length: int | None, precision: int | None) -> None:
        super().__init__(sql_type_name, length)

        self._validate_precision(precision)
        self._precision = precision

    def _validate_precision(self, precision: int) -> None:
        if not self._is_precision_valid(precision):
            raise InvalidPrecision(super().name)

    def _is_precision_valid(self, precision: int) -> bool:
        return (not super().length and precision is None) or \
            (super().length and not precision) or \
            (super().length and isinstance(precision, int) and precision >= 0 and precision < super().length)

    def _is_length_valid(self, length: int) -> bool:
        return length is None or (isinstance(length, int) and length > 0)

    @property
    def precision(self) -> int:
        return self._precision
