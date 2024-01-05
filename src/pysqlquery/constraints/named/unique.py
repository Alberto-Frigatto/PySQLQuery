'''
Defines the UniqueConstraint class for constructing named UNIQUE SQL constraint.
'''

from ..base import SingleColumnNamedConstraint


class UniqueConstraint(SingleColumnNamedConstraint):
    '''
    Represents a named UNIQUE constraint in SQL.

    This class inherits from `SingleColumnNamedConstraint` and provides functionality
    specific to the named UNIQUE constraint.
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

        Examples
        --------
        >>> un_const = UniqueConstraint('un_table_column', 'column')
        >>> print(un_const)
        CONSTRAINT un_table_column UNIQUE (column)
        '''

        super().__init__(name, column)

    def __str__(self) -> str:
        return f'CONSTRAINT {super().name} UNIQUE ({super().column})'
