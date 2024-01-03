from abc import ABCMeta
import re
from .named_constraint import NamedConstraint
from ..exceptions.named_constraint import InvalidColumnName


class SingleColumnNamedConstraint(NamedConstraint, metaclass=ABCMeta):
    def __init__(self, name: str, column: str) -> None:
        super().__init__(name)
        self._validate_column_name(column)
        self._column: str = column.strip().lower()

    def _validate_column_name(self, column_name: str) -> None:
        if not self._is_column_name_valid(column_name):
            raise InvalidColumnName(super().name, column_name)

    def _is_column_name_valid(self, column_name: str) -> bool:
        return isinstance(column_name, str) and re.search(r'^[a-zA-Z][a-zA-Z0-9_]*$', column_name)

    @property
    def column(self) -> str:
        return self._column
