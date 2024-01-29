import pytest

from src.pysqlquery.types import String
from src.pysqlquery.types.exceptions.sql_text_type import InvalidTypeLength


class TestString:
    def test_quando_nao_recebe_nada_retorna_VARCHAR(self) -> None:
        entry = String()
        expected = 'VARCHAR'
        result = str(entry)

        assert result == expected

    def test_quando_recebe_10_retorna_VARCHAR_10(self) -> None:
        entry = 10
        expected = 'VARCHAR(10)'
        string_type = String(entry)
        result = str(string_type)

        assert result == expected

    def test_quando_recebe_aaa_lanca_InvalidTypeLength(self) -> None:
        with pytest.raises(InvalidTypeLength):
            entry = 'aaa'
            String(entry)

    def test_quando_recebe_0_lanca_InvalidTypeLength(self) -> None:
        with pytest.raises(InvalidTypeLength):
            entry = 0
            String(entry)

    def test_quando_nao_recebe_nada_e_valida_alberto_retorna_True(self) -> None:
        entry = 'alberto'
        string_type = String()
        expected = True
        result = string_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_10_retorna_False(self) -> None:
        entry = 10
        string_type = String()
        expected = False
        result = string_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_abcd_retorna_True(self) -> None:
        entry = 'abcd'
        string_type = String(4)
        expected = True
        result = string_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_abcde_retorna_False(self) -> None:
        entry = 'abcde'
        string_type = String(4)
        expected = False
        result = string_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_abc_retorna_True(self) -> None:
        entry = 'abc'
        string_type = String(4)
        expected = True
        result = string_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_10_retorna_False(self) -> None:
        entry = 10
        string_type = String(4)
        expected = False
        result = string_type.validate_value(entry)

        assert result == expected
