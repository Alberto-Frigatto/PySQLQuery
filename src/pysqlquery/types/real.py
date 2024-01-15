'''
Defines the Real class for constructing REAL SQL type.
'''

from typing import Any

from .base import SQLDecimalType


class Real(SQLDecimalType):
    '''
    Represents a REAL data type in SQL.

    This class inherits from `SQLDecimalType` and provides functionality
    specific to the REAL data type.
    '''

    _TYPE_NAME = 'real'

    def __init__(self, precision: int | None = None, scale: int | None = None) -> None:
        '''
        Parameters
        ----------
        precision : int | None
            The precision of REAL type.
        scale : int | None
            The scale of REAL type (if passed it must be lower than precision).

        Returns
        -------
        None

        Examples
        --------
        >>> real_type = Real()
        >>> print(real_type)
        REAL

        >>> real_type = Real(6)
        >>> print(real_type)
        REAL(6)

        >>> real_type = Real(6, 2)
        >>> print(real_type)
        REAL(6, 2)
        '''

        super().__init__(self._TYPE_NAME, precision, scale)

    def __str__(self) -> str:
        rendered_value = super().name

        if super().precision:
            rendered_value += f'({super().precision}'

            if super().scale is not None:
                rendered_value += f', {super().scale}'

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
            True if the value is valid for the REAL SQL type, False otherwise.

        Examples
        --------
        >>> real_type = Real()
        >>> real_type.validate_value(10)
        True
        >>> real_type.validate_value(10.5)
        True

        >>> real_type = Real(2)
        >>> real_type.validate_value(10)
        True
        >>> real_type.validate_value(100)
        False

        >>> real_type = Real(3, 1)
        >>> real_type.validate_value(10)
        True
        >>> real_type.validate_value(100)
        True
        >>> real_type.validate_value(10.5)
        True
        >>> real_type.validate_value(1.55)
        False
        '''

        if not self._is_number(value):
            return False

        number_str = str(value)

        if super().precision:
            if not self._is_smaller_or_eq_than_the_precision_limit(number_str):
                return False

            if super().scale:
                DECIMAL_SEP = '.'

                pos_decimal_sep = number_str.find(DECIMAL_SEP)

                if pos_decimal_sep == -1:
                    return True

                qty_decimal_digits = len(number_str) - pos_decimal_sep - 1

                return self._is_smaller_or_eq_than_the_scale(qty_decimal_digits)

        return True

    def _is_number(self, value: Any) -> bool:
        return isinstance(value, (int, float))

    def _is_smaller_or_eq_than_the_precision_limit(self, number_str: str) -> bool:
        return len(number_str.replace('.', '')) <= super().precision

    def _is_smaller_or_eq_than_the_scale(self, qty_decimal_digits: int) -> bool:
        return qty_decimal_digits <= super().scale
