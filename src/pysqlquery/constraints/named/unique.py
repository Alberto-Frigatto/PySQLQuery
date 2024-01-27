'''
Defines the UniqueConstraint class for constructing named UNIQUE SQL constraint.
'''

from ..base import SingleColumnNamedConstraint


class UniqueConstraint(SingleColumnNamedConstraint):
    '''
    Represents a named UNIQUE constraint in SQL.

    This class can be used in table's __constraints__ list.

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
        >>>
        >>> class MyTable(Table):
        ...     my_column = Column(CHAR)
        ...     __constraints__ = [
        ...         UniqueConstraint('un_my_table_my_column', 'my_column')
        ...     ]
        ...
        >>> my_table = MyTable()
        >>> print(my_table.my_column.unique)
        >>> True
        '''

        super().__init__(name, column)

    def __str__(self) -> str:
        return f'CONSTRAINT {super().name} UNIQUE ({super().column})'
