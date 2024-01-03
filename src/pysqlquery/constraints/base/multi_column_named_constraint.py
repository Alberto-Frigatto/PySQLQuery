from abc import ABCMeta
import re
from .named_constraint import NamedConstraint
from ..exceptions.multi_column_named_constraint import InvalidColumnType
from ..exceptions.named_constraint import InvalidColumnName


class MultiColumnNamedConstraint(NamedConstraint, metaclass=ABCMeta):
    def __init__(self, name: str, column: str | list[str]) -> None:
        super().__init__(name)
        self._validate_column(column)
        self._column: str | list[str] = self._handle_column(column)

    def _validate_column(self, column: str | list[str]) -> None:
        if not self._is_column_of_a_allowed_type(column):
            raise InvalidColumnType(super().name, column)

        if not len(column):
            raise InvalidColumnName(super().name, column)

        if isinstance(column, str) and not self._is_column_name_valid(column):
            raise InvalidColumnName(super().name, column)
        elif isinstance(column, list):
            for column_name in column:
                if not self._is_column_name_valid(column_name):
                    raise InvalidColumnName(super().name, column_name)

    def _is_column_of_a_allowed_type(self, column: str | list[str]) -> bool:
        return isinstance(column, (str, list))

    def _is_column_name_valid(self, column_name: str) -> bool:
        return isinstance(column_name, str) and bool(re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', column_name))

    def _handle_column(self, column: str | list[str]) -> str | list[str]:
        if isinstance(column, str):
            return column.strip().lower()
        else:
            if len(column) == 1:
                return column[0].strip().lower()
            else:
                return [column_name.strip().lower() for column_name in column]

    @property
    def column(self) -> str | list[str]:
        return self._column
