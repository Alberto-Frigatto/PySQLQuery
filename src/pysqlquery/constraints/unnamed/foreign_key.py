'''
Defines the ForeignKey class for constructing unnamed FOREIGN KEY SQL constraint.
'''

import re
from typing import Literal

from ..base import UnnamedConstraint
from ..exceptions.unnamed_foreign_key import (
    InvalidOnDeleteClause,
    InvalidOnUpdateClause,
    InvalidRefColumn,
    InvalidRefTable,
    MissingColumnName,
)


class ForeignKey(UnnamedConstraint):
    '''
    Represents a unnamed FOREIGN KEY constraint in SQL.

    This class must be used in a table's column.

    This class inherits from `UnnamedConstraint` and provides functionality
    specific to the unnamed FOREIGN KEY constraint.
    '''

    def __init__(
        self,
        ref_table: str,
        ref_column: str,
        *,
        on_delete: Literal['cascade', 'set null', 'set default', 'no action', 'restrict']
        | None = None,
        on_update: Literal['cascade', 'set null', 'set default', 'no action', 'restrict']
        | None = None,
    ) -> None:
        '''
        Parameters
        ----------
        ref_table : str
            The referenced table.
        ref_column : str
            The referenced column name.
        on_delete : str | None
            The ON DELETE clause.
        on_update : str | None
            The ON UPDATE clause.

        Returns
        -------
        None

        Examples
        --------
        >>> class MyTable(Table):
        >>> ... fk_col = Column(Integer, ForeignKey('other_table', 'id'))
        >>> ...
        >>> my_table = MyTable()
        >>> print(my_table.fk_col.foreign_key)
        >>> FOREIGN KEY (fk_col) REFERENCES OTHER_TABLE(id)
        >>>
        >>> class MyTable(Table):
        >>> ... fk_col = Column(Integer, ForeignKey('other_table', 'id', on_delete='cascade', on_update='no action'))
        >>> ...
        >>> my_table = MyTable()
        >>> print(my_table.fk_col.foreign_key)
        >>> FOREIGN KEY (fk_col) REFERENCES OTHER_TABLE(id) ON DELETE CASCADE ON UPDATE NO ACTION
        '''

        self._validate_ref_table(ref_table)
        self._ref_table: str = ref_table.strip().lower()

        self._validate_ref_column(ref_column)
        self._ref_column: str = ref_column.strip().lower()

        self._validate_on_delete(on_delete)
        self._on_delete: str | None = self._handle_on_clause(on_delete)

        self._validate_on_update(on_update)
        self._on_update: str | None = self._handle_on_clause(on_update)

        super().__init__()

    def _validate_ref_table(self, ref_table: str) -> None:
        if not self._is_ref_table_valid(ref_table):
            raise InvalidRefTable(ref_table)

    def _is_ref_table_valid(self, ref_table: str) -> bool:
        return isinstance(ref_table, str) and re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', ref_table)

    def _validate_ref_column(self, ref_column: str) -> None:
        if not self._is_ref_column_valid(ref_column):
            raise InvalidRefColumn(self._ref_table, ref_column)

    def _is_ref_column_valid(self, ref_column: str) -> bool:
        return isinstance(ref_column, str) and re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', ref_column)

    def _validate_on_delete(self, on_delete: str | None) -> None:
        if not self._is_on_clause_valid(on_delete):
            raise InvalidOnDeleteClause(self._ref_table, self._ref_column, on_delete)

    def _is_on_clause_valid(self, on_clause: str | None) -> bool:
        allowed_kinds_of_on_clause = ('cascade', 'set null', 'set default', 'no action', 'restrict')

        return (
            on_clause is None
            or isinstance(on_clause, str)
            and on_clause.strip().lower() in allowed_kinds_of_on_clause
        )

    def _validate_on_update(self, on_update: str | None) -> None:
        if not self._is_on_clause_valid(on_update):
            raise InvalidOnUpdateClause(self._ref_table, self._ref_column, on_update)

    def _handle_on_clause(self, on_clause: str | None) -> str | None:
        return on_clause.strip().lower() if on_clause else None

    def __str__(self) -> str:
        if not super().column:
            raise MissingColumnName(self._ref_table, self._ref_column)

        reference_str = f'{self._ref_table.upper()}({self._ref_column})'

        fk_repr = f'FOREIGN KEY ({super().column}) REFERENCES {reference_str}'

        fk_repr += f' ON DELETE {self._on_delete.upper()}' if self._on_delete else ''
        fk_repr += f' ON UPDATE {self._on_update.upper()}' if self._on_update else ''

        return fk_repr

    @property
    def ref_table(self) -> str:
        return self._ref_table

    @property
    def ref_column(self) -> str:
        return self._ref_column

    @property
    def on_delete(self) -> str | None:
        return self._on_delete

    @property
    def on_update(self) -> str | None:
        return self._on_update
