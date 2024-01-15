'''
Defines the abstract base class for constructing decimal SQL type classes.
'''

from abc import ABCMeta

from ..exceptions.sql_decimal_type import InvalidScale
from .sql_num_type import SQLNumType


class SQLDecimalType(SQLNumType, metaclass=ABCMeta):
    '''
    Abstract class for construct decimal SQL type classes.

    This class inherits from `SQLNumType` and provides the basic structures for construct
    concrete classes that represents decimal SQL types or another
    abstract classes for other kind of decimal SQL types.

    This class must be inherited by concrete or another abstract one.
    '''

    def __init__(self, sql_type_name: str, precision: int | None, scale: int | None) -> None:
        '''
        Parameters
        ----------
        sql_type_name : str
            The name of decimal SQL type.
        precision : int | None
            The precision of decimal SQL type.
        precision : int | None
            The precision of decimal SQL type (if passed it must be lower than length).

        Returns
        -------
        None
        '''

        super().__init__(sql_type_name, precision)

        self._validate_scale(scale)
        self._scale: int | None = scale

    def _validate_scale(self, scale: int | None) -> None:
        if not self._is_scale_valid(scale):
            raise InvalidScale(super().name, scale)

    def _is_scale_valid(self, scale: int | None) -> bool:
        return (not super().precision and scale is None) or (
            super().precision
            and (not scale or isinstance(scale, int) and 0 <= scale < super().precision)
        )

    @property
    def scale(self) -> int | None:
        return self._scale
