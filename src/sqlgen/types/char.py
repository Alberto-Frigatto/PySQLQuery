from .base import BaseType


class Char(BaseType):
    _TYPE_NAME = 'char'

    def __init__(self, length: int = 1) -> None:
        super().__init__(self._TYPE_NAME, length)

    def _is_length_valid(self, length: int) -> bool:
        return isinstance(length, int) and length > 0

    def __str__(self) -> str:
        rendered_value = super().name

        if super().length:
            rendered_value += f'({super().length})'

        return rendered_value

    def validate_value(self, value: str) -> bool:
        return isinstance(value, str) and len(value) <= super().length
