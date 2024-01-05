'''
Defines the abstract base class for constructing unnamed SQL constraint classes.
'''

from abc import ABCMeta
import re
from ..exceptions.unnamed_constraint import InvalidAddedColumnName
from .constraint import Constraint


class UnnamedConstraint(Constraint, metaclass=ABCMeta):
    '''
    Abstract class for construct unnamed SQL constraint classes.

    This class inherits from `Constraint` and provides the basic structures for construct
    concrete classes that represents unnamed SQL constraints or another
    abstract classes for other kind of unnamed SQL constraints.

    This class must be inherited by concrete or another abstract one.
    '''

    def __init__(self) -> None:
        super().__init__()
        self._column_name: str = None

    def add_column_name(self, column_name: str) -> None:
        '''
        Adds the column's name that this constraint belongs to.

        `This method shouldn't be used`. It's used by `pysqlquery` automatically when you adds
        '''

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
