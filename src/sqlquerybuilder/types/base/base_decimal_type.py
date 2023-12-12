'''
Defines the abstract base class for constructing decimal SQL type classes.
'''

from abc import ABCMeta
from . import BaseType
from sqlquerybuilder.types.exceptions.base_decimal_type import InvalidPrecision


class BaseDecimalType(BaseType, metaclass=ABCMeta):
    '''
    Abstract class for construct decimal SQL type classes.

    This class inherits from `BaseType` and provides the basic structures for construct
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
        self._precision = precision

    def _validate_precision(self, precision: int) -> None:
        if not self._is_precision_valid(precision):
            raise InvalidPrecision(super().name)

    def _is_precision_valid(self, precision: int) -> bool:
        return (not super().length and precision is None) or \
            (super().length and not precision) or \
            (super().length and isinstance(precision, int) and precision >= 0 and precision < super().length)

    def _is_length_valid(self, length: int) -> bool:
        return length is None or (isinstance(length, int) and length > 0)

    @property
    def precision(self) -> int:
        return self._precision
