'''
Defines the abstract base class for constructing single column named SQL constraint classes.
'''

from abc import ABCMeta
import re
from .named_constraint import NamedConstraint
from ..exceptions.named_constraint import InvalidColumnName


class SingleColumnNamedConstraint(NamedConstraint, metaclass=ABCMeta):
    '''
    Abstract class for construct single column named SQL constraint classes.

    This class inherits from `NamedConstraint` and provides the basic structures for construct
    concrete classes that represents single column named SQL constraints or another
    abstract classes for other kind of single column named SQL constraints.

    This class must be inherited by concrete or another abstract one.
    '''

    def __init__(self, name: str, column: str) -> None:
        '''
        Parameters
        ----------
        name : str
            The constraint's name.
        column : str
            The column's name that this constraint belongs to.

        Returns
        -------
        None
        '''

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
