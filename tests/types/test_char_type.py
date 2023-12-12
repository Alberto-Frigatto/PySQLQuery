import pytest
from src.pysqlquery.types import Char


class TestChar:
    def test_quando_nao_recebe_nada_retorna_CHAR(self) -> None:
        entry = Char()
        expected = 'CHAR'
        result = str(entry)

        assert result == expected

    def test_quando_recebe_3_retorna_CHAR_3(self) -> None:
        entry = 3
        expected = 'CHAR(3)'
        char_type = Char(entry)
        result = str(char_type)

        assert result == expected

    def test_quando_recebe_aaa_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry = 'aaa'
            Char(entry)

    def test_quando_recebe_0_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry = 0
            Char(entry)

    def test_quando_nao_recebe_nada_e_valida_a_retorna_True(self) -> None:
        entry = 'a'
        char_type = Char()
        expected = True
        result = char_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_abc_retorna_False(self) -> None:
        entry = 'abc'
        char_type = Char()
        expected = False
        result = char_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_10_retorna_False(self) -> None:
        entry = 10
        char_type = Char()
        expected = False
        result = char_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_abcd_retorna_True(self) -> None:
        entry = 'abcd'
        char_type = Char(4)
        expected = True
        result = char_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_abcde_retorna_False(self) -> None:
        entry = 'abcde'
        char_type = Char(4)
        expected = False
        result = char_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_abc_retorna_True(self) -> None:
        entry = 'abc'
        char_type = Char(4)
        expected = True
        result = char_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_4_e_valida_10_retorna_False(self) -> None:
        entry = 10
        char_type = Char(4)
        expected = False
        result = char_type.validate_value(entry)

        assert result == expected
