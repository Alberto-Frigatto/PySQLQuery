import pytest

from src.pysqlquery.types import Integer
from src.pysqlquery.types.exceptions.sql_num_type import InvalidPrecision


class TestInteger:
    def test_quando_nao_recebe_nada_retorna_INTEGER(self) -> None:
        entry = Integer()
        expected = 'INTEGER'
        result = str(entry)

        assert result == expected

    def test_quando_recebe_2_retorna_INTEGER_2(self) -> None:
        entry = 2
        int_type = Integer(entry)
        expected = 'INTEGER(2)'
        result = str(int_type)

        assert result == expected

    def test_quando_recebe_aaa_lanca_InvalidPrecision(self) -> None:
        with pytest.raises(InvalidPrecision):
            entry = 'aaa'
            Integer(entry)

    def test_quando_recebe_0_lanca_InvalidPrecision(self) -> None:
        with pytest.raises(InvalidPrecision):
            entry = 0
            Integer(entry)

    def test_quando_nao_recebe_nada_e_valida_6e7_int_retorna_True(self) -> None:
        entry = int(6e7)
        int_type = Integer()
        expected = True
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        int_type = Integer()
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_2_e_valida_65_int_retorna_True(self) -> None:
        entry = 65
        int_type = Integer(2)
        expected = True
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_2_e_valida_4_float_retorna_False(self) -> None:
        entry = 4.0
        int_type = Integer(2)
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_2_e_valida_350_int_retorna_False(self) -> None:
        entry = 350
        int_type = Integer(2)
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_2_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        int_type = Integer(2)
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected
