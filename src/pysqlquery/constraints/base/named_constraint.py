from abc import ABCMeta
import re
from .constraint import Constraint
from ..exceptions.named_constraint import InvalidConstraintName


class NamedConstraint(Constraint, metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._validate_name(name)
        self._name: str = name.lower()

    def _validate_name(self, name: str) -> None:
        if not self._is_name_valid(name):
            raise InvalidConstraintName(name)

    def _is_name_valid(self, name: str) -> bool:
        return isinstance(name, str) and re.search(r'^[a-zA-Z][a-zA-Z0-9_]*$', name)

    @property
    def name(self) -> str:
        return self._name
