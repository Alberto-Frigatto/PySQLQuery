from typing import Any
import pytest
from src.pysqlquery.types.base import (
    SQLDateType,
    SQLTextType
)
from src.pysqlquery.types.exceptions.sql_type import InvalidTypeName
from src.pysqlquery.types.exceptions.sql_date_type import InvalidDatePattern


class TestNewType:
    @pytest.fixture
    def my_textual_type(self):
        class MyTextualType(SQLTextType):
            _TYPE_NAME = 'NEWTEXTTYPE'
            def __init__(self, length: int | None = None) -> None:
                super().__init__(self._TYPE_NAME, length)

            def __str__(self) -> str:
                rendered_value = super().name

                if super().length:
                    rendered_value += f'({super().length})'

                return rendered_value

            def validate_value(self, value: str) -> bool:
                return isinstance(value, str)

        return MyTextualType

    def test_quando_MyTextualType_nao_recebe_nada_retorna_NEWTEXTTYPE(self, my_textual_type) -> None:
        entry = my_textual_type()
        expected = 'NEWTEXTTYPE'
        result = str(entry)

        assert result == expected

    def test_quando_MyTextualType_recebe_20_retorna_NEWTEXTTYPE_20(self, my_textual_type) -> None:
        entry = my_textual_type(20)
        expected = 'NEWTEXTTYPE(20)'
        result = str(entry)

        assert result == expected

    def test_quando_criamos_novo_tipo_com_nome_69_lanca_InvalidTypeName(self) -> None:
        class NewDateType(SQLDateType):
            _TYPE_NAME = 69

            def __init__(self) -> None:
                DATE_PATTERN = '%Y'
                super().__init__(self._TYPE_NAME, DATE_PATTERN)

            def __str__(self) -> str:
                rendered_value = super().name

                return rendered_value

            def validate_value(self, value: str) -> bool:
                return True

        with pytest.raises(InvalidTypeName):
            NewDateType()

    def test_quando_criamos_novo_tipo_com_nome_None_lanca_InvalidTypeName(self) -> None:
        class NewDateType(SQLDateType):
            _TYPE_NAME = None

            def __init__(self) -> None:
                DATE_PATTERN = '%Y'
                super().__init__(self._TYPE_NAME, DATE_PATTERN)

            def __str__(self) -> str:
                rendered_value = super().name

                return rendered_value

            def validate_value(self, value: str) -> bool:
                return True

        with pytest.raises(InvalidTypeName):
            NewDateType()

    def test_quando_criamos_novo_tipo_com_nome_str_vazia_lanca_InvalidTypeName(self) -> None:
        class NewDateType(SQLDateType):
            _TYPE_NAME = ''

            def __init__(self) -> None:
                DATE_PATTERN = '%Y'
                super().__init__(self._TYPE_NAME, DATE_PATTERN)

            def __str__(self) -> str:
                rendered_value = super().name

                return rendered_value

            def validate_value(self, value: str) -> bool:
                return True

        with pytest.raises(InvalidTypeName):
            NewDateType()

    def test_quando_criamos_novo_tipo_de_data_com_pattern_aaa_lanca_InvalidDatePattern(self) -> None:
        class NewDateType(SQLDateType):
            _TYPE_NAME = 'NEWDATETYPE'

            def __init__(self) -> None:
                DATE_PATTERN = 'aaa'
                super().__init__(self._TYPE_NAME, DATE_PATTERN)

            def __str__(self) -> str:
                rendered_value = super().name

                return rendered_value

            def validate_value(self, value: str) -> bool:
                return True

        with pytest.raises(InvalidDatePattern):
            NewDateType()

    def test_quando_criamos_novo_tipo_de_data_com_pattern_123_lanca_InvalidDatePattern(self) -> None:
        class NewDateType(SQLDateType):
            _TYPE_NAME = 'NEWDATETYPE'

            def __init__(self) -> None:
                DATE_PATTERN = 123
                super().__init__(self._TYPE_NAME, DATE_PATTERN)

            def __str__(self) -> str:
                rendered_value = super().name

                return rendered_value

            def validate_value(self, value: str) -> bool:
                return True

        with pytest.raises(InvalidDatePattern):
            NewDateType()

    def test_quando_criamos_algum_tipo_novo_e_nao_implementamos_os_metodos__str__e_validate_value_lanca_TypeError(self) -> None:
        class NewType(SQLTextType):
            _TYPE_NAME = 'TYPE'

            def __init__(self, length: int | None = None) -> None:
                super().__init__(self._TYPE_NAME, length)

        with pytest.raises(TypeError):
            NewType()
