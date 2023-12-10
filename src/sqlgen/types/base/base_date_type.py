import re
from . import BaseType
from sqlgen.types.exceptions.base_date_type import InvalidDatePattern


class BaseDateType(BaseType):
    def __init__(self, sql_type_name: str, date_pattern: str) -> None:
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
