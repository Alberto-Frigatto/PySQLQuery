'''
Defines the PrimaryKeyConstraint class for constructing named PRIMARY KEY SQL constraint.
'''

from ..base import MultiColumnNamedConstraint


class PrimaryKeyConstraint(MultiColumnNamedConstraint):
    '''
    Represents a named PRIMARY KEY constraint in SQL.

    This class inherits from `MultiColumnNamedConstraint` and provides functionality
    specific to the named PRIMARY KEY constraint.
    '''

    def __init__(self, name: str, column: str | list[str]) -> None:
        '''
        Parameters
        ----------
        name : str
            The constraint's name.
        column : str | list[str]
            The column's name(s) that this constraint belongs to.

        Returns
        -------
        None

        Examples
        --------
        >>> pk_const = PrimaryKeyConstraint('pk_table', 'id')
        >>> print(pk_const)
        CONSTRAINT pk_table PRIMARY KEY (id)
        >>>
        >>> pk_const = PrimaryKeyConstraint('pk_table', ['id_1', 'id_2'])
        >>> print(pk_const)
        CONSTRAINT pk_table PRIMARY KEY (id_1, id_2)
        '''

        super().__init__(name, column)

    def __str__(self) -> str:
        pk_repr = (f'CONSTRAINT {super().name} PRIMARY KEY '
                    f'({super().column if isinstance(super().column, str) else ", ".join(super().column)})')

        return pk_repr
