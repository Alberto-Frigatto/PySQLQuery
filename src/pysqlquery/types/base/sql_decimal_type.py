'''
Defines the abstract base class for constructing decimal SQL type classes.
'''

from abc import ABCMeta

from ..exceptions.sql_decimal_type import InvalidPrecision
from .sql_num_type import SQLNumType


class SQLDecimalType(SQLNumType, metaclass=ABCMeta):
    '''
    Abstract class for construct decimal SQL type classes.

    This class inherits from `SQLNumType` and provides the basic structures for construct
    concrete classes that represents decimal SQL types or another
    abstract classes for other kind of decimal SQL types.

    This class must be inherited by concrete or another abstract one.
    '''

    def __init__(self, sql_type_name: str, length: int | None, precision: int | None) -> None:
        '''
        Parameters
        ----------
        sql_type_name : str
            The name of decimal SQL type.
        length : int | None
            The length of decimal SQL type.
        precision : int | None
            The precision of decimal SQL type (if passed it must be lower than length).

        Returns
        -------
        None
        '''

        super().__init__(sql_type_name, length)

        self._validate_precision(precision)
        self._precision: int | None = precision

    def _validate_precision(self, precision: int | None) -> None:
        if not self._is_precision_valid(precision):
            raise InvalidPrecision(super().name, precision)

    def _is_precision_valid(self, precision: int | None) -> bool:
        return (not super().length and precision is None) or (
            super().length
            and (not precision or isinstance(precision, int) and 0 <= precision < super().length)
        )

    @property
    def precision(self) -> int | None:
        return self._precision
