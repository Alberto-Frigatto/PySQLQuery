'''
Defines the ForeignKeyConstraint class for constructing named FOREIGN KEY SQL constraint.
'''

import re
from typing import Literal
from ..base import MultiColumnNamedConstraint
from ..exceptions.named_foreign_key import (
    InvalidOnDeleteClause,
    InvalidOnUpdateClause,
    InvalidRefColumnType,
    InvalidRefColumn,
    InvalidRefTable,
    InvalidRefColumnListLength,
    RefColumnMustBeStr,
    RefColumnMustBeList
)


class ForeignKeyConstraint(MultiColumnNamedConstraint):
    '''
    Represents a named FOREIGN KEY constraint in SQL.

    This class inherits from `MultiColumnNamedConstraint` and provides functionality
    specific to the named FOREIGN KEY constraint.
    '''

    def __init__(
        self,
        name: str,
        column: str | list[str],
        ref_table: str,
        ref_column: str | list[str],
        *,
        on_delete: Literal['cascade', 'set null', 'set default', 'no action', 'restrict'] | None = None,
        on_update: Literal['cascade', 'set null', 'set default', 'no action', 'restrict'] | None = None
    ) -> None:
        '''
        Parameters
        ----------
        name : str
            The constraint's name.
        column : str | list[str]
            The column's name(s) that this constraint belongs to.
        ref_table : str
            The referenced table.
        ref_column : str | list[str]
            The referenced column name(s) (this must be the same type than column parameter).
        on_delete : str | None
            The ON DELETE clause.
        on_update : str | None
            The ON UPDATE clause.

        Returns
        -------
        None

        Examples
        --------
        >>> fk_const = ForeignKeyConstraint('fk_table_other_table', 'fk_col', 'other_table', 'id')
        >>> print(fk_const)
        CONSTRAINT fk_table_other_table FOREIGN KEY (fk_col) REFERENCES OTHER_TABLE(id)
        >>>
        >>> fk_const = ForeignKeyConstraint('fk_table_other_table', 'fk_col', 'other_table', 'id', on_delete='cascade', on_update='no action')
        >>> print(fk_const)
        CONSTRAINT fk_table_other_table FOREIGN KEY (fk_col) REFERENCES OTHER_TABLE(id) ON DELETE CASCADE ON UPDATE NO ACTION
        >>>
        >>> fk_const = ForeignKeyConstraint('fk_table_other_table', ['fk_col_1', 'fk_col_2'], 'other_table', ['id_1', 'id_2'])
        >>> print(fk_const)
        CONSTRAINT fk_table_other_table FOREIGN KEY (fk_col_1, fk_col_2) REFERENCES OTHER_TABLE(id_1, id_2)
        '''

        super().__init__(name, column)

        self._validate_ref_table(ref_table)
        self._ref_table: str = ref_table.strip().lower()

        self._validate_ref_column(ref_column)
        self._ref_column: str | list[str] = self._handle_ref_column(ref_column)

        self._validate_on_delete(on_delete)
        self._on_delete: str | None = self._handle_on_clause(on_delete)

        self._validate_on_update(on_update)
        self._on_update: str | None = self._handle_on_clause(on_update)

    def _validate_ref_table(self, ref_table: str) -> None:
        if not self._is_ref_table_valid(ref_table):
            raise InvalidRefTable(super().name, ref_table)

    def _is_ref_table_valid(self, ref_table: str) -> bool:
        return isinstance(ref_table, str) and re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', ref_table)

    def _validate_ref_column(self, ref_column: str | list[str]) -> None:
        if not super()._is_column_of_a_allowed_type(ref_column):
            raise InvalidRefColumnType(super().name, ref_column)

        if isinstance(ref_column, str):
            if isinstance(super().column, list):
                raise RefColumnMustBeList(super().name)
            elif not super()._is_column_name_valid(ref_column):
                raise InvalidRefColumn(super().name, ref_column)
        elif isinstance(ref_column, list):
            if isinstance(super().column, str):
                raise RefColumnMustBeStr(super().name)
            elif len(ref_column) != len(super().column):
                raise InvalidRefColumnListLength(super().name, len(ref_column), len(super().column))

            for column_name in ref_column:
                if not super()._is_column_name_valid(column_name):
                    raise InvalidRefColumn(super().name, column_name)

    def _validate_on_delete(self, on_delete: str | None) -> None:
        if not self._is_on_clause_valid(on_delete):
            raise InvalidOnDeleteClause(super().name, on_delete)

    def _is_on_clause_valid(self, on_clause: str | None) -> bool:
        allowed_kinds_of_on_clause = (
            'cascade',
            'set null',
            'set default',
            'no action',
            'restrict'
        )

        return on_clause is None or \
            isinstance(on_clause, str) and on_clause.strip().lower() in allowed_kinds_of_on_clause

    def _validate_on_update(self, on_update: str | None) -> None:
        if not self._is_on_clause_valid(on_update):
            raise InvalidOnUpdateClause(super().name, on_update)

    def _handle_ref_column(self, ref_column: str | list[str]) -> str | list[str]:
        return ref_column.lower() if isinstance(ref_column, str) else \
            [ref_column_name.strip().lower() for ref_column_name in ref_column]

    def _handle_on_clause(self, on_clause: str | None) -> str | None:
        return on_clause.strip().lower() if on_clause else None

    def __str__(self) -> str:
        fk_repr = (f'CONSTRAINT {super().name} FOREIGN KEY '
                    f'({super().column if isinstance(super().column, str) else ", ".join(super().column)}) '
                    f'REFERENCES {self._ref_table.upper()}({self._ref_column if isinstance(self._ref_column, str) else ", ".join(self._ref_column)})')

        fk_repr += f' ON DELETE {self._on_delete.upper()}' if self._on_delete else ''
        fk_repr += f' ON UPDATE {self._on_update.upper()}' if self._on_update else ''

        return fk_repr

    @property
    def ref_table(self) -> str:
        return self._ref_table

    @property
    def ref_column(self) -> str | list[str]:
        return self._ref_column

    @property
    def on_delete(self) -> str | None:
        return self._on_delete

    @property
    def on_update(self) -> str | None:
        return self._on_update
