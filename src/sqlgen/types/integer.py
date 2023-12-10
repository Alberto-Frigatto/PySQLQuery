from .base import BaseType


class Integer(BaseType):
    _TYPE_NAME = 'integer'

    def __init__(self, length: int | None = None) -> None:
        super().__init__(self._TYPE_NAME, length)

    def __str__(self) -> str:
        rendered_value = super().name

        if super().length:
            rendered_value += f'({super().length})'

        return rendered_value

    def validate_value(self, value: int) -> bool:
        return isinstance(value, int) and (len(str(value)) <= super().length if super().length else True)
