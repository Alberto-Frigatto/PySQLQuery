from abc import ABCMeta
import re
from ..exceptions.unnamed_constraint import InvalidAddedColumnName
from .constraint import Constraint


class UnnamedConstraint(Constraint, metaclass=ABCMeta):
    def __init__(self) -> None:
        super().__init__()
        self._column_name: str = None

    def add_column_name(self, column_name: str) -> None:
        self._validate_column_name(column_name)
        self._column_name = column_name

    def _validate_column_name(self, column_name: str) -> None:
        if not self._is_column_name_valid(column_name):
            raise InvalidAddedColumnName(column_name)

    def _is_column_name_valid(self, column_name: str) -> bool:
        return isinstance(column_name, str) and re.search(r'^[a-zA-Z][a-zA-Z0-9_]*$', column_name)

    @property
    def column(self)-> str:
        return self._column_name
