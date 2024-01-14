'''
Defines the Decimal class for constructing DECIMAL SQL type.
'''

from typing import Any

from .base import SQLDecimalType


class Decimal(SQLDecimalType):
    '''
    Represents a DECIMAL data type in SQL.

    This class inherits from `SQLDecimalType` and provides functionality
    specific to the DECIMAL data type.
    '''

    _TYPE_NAME = 'decimal'

    def __init__(self, length: int | None = None, precision: int | None = None) -> None:
        '''
        Parameters
        ----------
        length : int | None
            The length of DECIMAL type.
        precision : int | None
            The precision of DECIMAL type (if passed it must be lower than length).

        Returns
        -------
        None

        Examples
        --------
        >>> decimal_type = Decimal()
        >>> print(decimal_type)
        DECIMAL

        >>> decimal_type = Decimal(6)
        >>> print(decimal_type)
        DECIMAL(6)

        >>> decimal_type = Decimal(6, 2)
        >>> print(decimal_type)
        DECIMAL(6, 2)
        '''

        super().__init__(self._TYPE_NAME, length, precision)

    def __str__(self) -> str:
        rendered_value = super().name

        if super().length:
            rendered_value += f'({super().length}'

            if super().precision is not None:
                rendered_value += f', {super().precision}'

            rendered_value += ')'

        return rendered_value

    def validate_value(self, value: float | int) -> bool:
        '''
        Parameters
        ----------
        value : float | int
            The value to be validated.

        Returns
        -------
        bool
            True if the value is valid for the DECIMAL SQL type, False otherwise.

        Examples
        --------
        >>> decimal_type = DECIMAL()
        >>> decimal_type.validate_value(10)
        True
        >>> decimal_type.validate_value(10.5)
        True

        >>> decimal_type = DECIMAL(2)
        >>> decimal_type.validate_value(10)
        True
        >>> decimal_type.validate_value(100)
        False

        >>> decimal_type = DECIMAL(3, 1)
        >>> decimal_type.validate_value(10)
        True
        >>> decimal_type.validate_value(100)
        True
        >>> decimal_type.validate_value(10.5)
        True
        >>> decimal_type.validate_value(1.55)
        False
        '''

        if not self._is_number(value):
            return False

        number_str = str(value)

        if super().length:
            if not self._is_smaller_or_eq_than_the_length_limit(number_str):
                return False

            if super().precision:
                DECIMAL_SEP = '.'

                pos_decimal_sep = number_str.find(DECIMAL_SEP)

                if pos_decimal_sep == -1:
                    return True

                qty_decimal_digits = len(number_str) - pos_decimal_sep - 1

                return self._is_smaller_or_eq_than_the_precision(qty_decimal_digits)

        return True

    def _is_number(self, value: Any) -> bool:
        return isinstance(value, (int, float))

    def _is_smaller_or_eq_than_the_length_limit(self, number_str: str) -> bool:
        return len(number_str.replace('.', '')) <= super().length

    def _is_smaller_or_eq_than_the_precision(self, qty_decimal_digits: int) -> bool:
        return qty_decimal_digits <= super().precision
