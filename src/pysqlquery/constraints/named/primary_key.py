from ..base import MultiColumnNamedConstraint


class PrimaryKeyConstraint(MultiColumnNamedConstraint):
    def __init__(self, name: str, column: str | list[str]) -> None:
        super().__init__(name, column)

    def __str__(self) -> str:
        pk_repr = (f'CONSTRAINT {super().name} PRIMARY KEY '
                    f'({super().column if isinstance(super().column, str) else ", ".join(super().column)})')

        return pk_repr
