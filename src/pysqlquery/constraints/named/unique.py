from ..base import SingleColumnNamedConstraint


class UniqueConstraint(SingleColumnNamedConstraint):
    def __init__(self, name: str, column: str) -> None:
        super().__init__(name, column)

    def __str__(self) -> str:
        return f'CONSTRAINT {super().name} UNIQUE ({super().column})'
