'''
Defines the abstract base class for constructing numeric SQL type classes.
'''

from abc import ABCMeta

from ..exceptions.sql_num_type import InvalidPrecision
from .sql_type import SQLType


class SQLNumType(SQLType, metaclass=ABCMeta):
    '''
    Abstract class for construct numeric SQL type classes.

    This class inherits from `SQLType` and provides the basic structures for construct
    another abstract classes for other kind of numeric SQL types.

    This class must be inherited by abstract one.
    '''

    def __init__(self, sql_type_name: str, precision: int | None) -> None:
        '''
        Parameters
        ----------
        sql_type_name : str
            The name of SQL type.
        precision : int | None
            The precision of SQL type.

        Returns
        -------
        None
        '''

        super().__init__(sql_type_name)

        self._validate_precision(precision)
        self._precision: int | None = precision

    def _validate_precision(self, precision: int | None) -> None:
        if not self._is_precision_valid(precision):
            raise InvalidPrecision(super().name, precision)

    def _is_precision_valid(self, precision: int | None) -> bool:
        return precision is None or (isinstance(precision, int) and precision > 0)

    @property
    def precision(self) -> int | None:
        return self._precision
