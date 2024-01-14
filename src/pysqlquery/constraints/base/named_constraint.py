'''
Defines the abstract base class for constructing named SQL constraint classes.
'''

import re
from abc import ABCMeta

from ..exceptions.named_constraint import InvalidConstraintName
from .constraint import Constraint


class NamedConstraint(Constraint, metaclass=ABCMeta):
    '''
    Abstract class for construct named SQL constraint classes.

    This class inherits from `Constraint` and provides the basic structures for construct
    abstract classes for kind of named SQL constraints.

    This class must be inherited by abstract one.
    '''

    def __init__(self, name: str) -> None:
        '''
        Parameters
        ----------
        name : str
            The constraint's name.

        Returns
        -------
        None
        '''

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
