import pytest

from src.pysqlquery.types import Decimal
from src.pysqlquery.types.exceptions.sql_decimal_type import InvalidScale
from src.pysqlquery.types.exceptions.sql_num_type import InvalidPrecision


class TestDecimal:
    def test_quando_nao_recebe_nada_retorna_DECIMAL(self) -> None:
        entry = Decimal()
        expected = 'DECIMAL'
        result = str(entry)

        assert result == expected

    def test_quando_recebe_precision_4_retorna_DECIMAL_4(self) -> None:
        entry = 4
        expected = 'DECIMAL(4)'
        float_type = Decimal(entry)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_retorna_DECIMAL_4_2(self) -> None:
        entry_precision = 4
        entry_scale = 2
        expected = 'DECIMAL(4, 2)'
        float_type = Decimal(entry_precision, entry_scale)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_precision_aaa_lanca_InvalidPrecision(self) -> None:
        with pytest.raises(InvalidPrecision):
            entry = 'aaa'
            Decimal(entry)

    def test_quando_recebe_precision_0_lanca_InvalidPrecision(self) -> None:
        with pytest.raises(InvalidPrecision):
            entry = 0
            Decimal(entry)

    def test_quando_recebe_scale_aaa_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry = 'aaa'
            Decimal(scale=entry)

    def test_quando_recebe_scale_0_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry = 0
            Decimal(scale=entry)

    def test_quando_recebe_scale_4_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry = 4
            Decimal(scale=entry)

    def test_quando_recebe_precision_4_e_scale_0_retorna_DECIMAL_4_0(self) -> None:
        entry_precision = 4
        entry_scale = 0
        expected = 'DECIMAL(4, 0)'
        float_type = Decimal(entry_precision, entry_scale)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_4_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry_precision = 4
            entry_scale = 4
            Decimal(entry_precision, entry_scale)

    def test_quando_recebe_precision_4_e_scale_aaa_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry_precision = 4
            entry_scale = 'aaa'
            Decimal(entry_precision, entry_scale)

    def test_quando_nao_recebe_nada_e_valida_6e7_int_retorna_True(self) -> None:
        entry = int(6e7)
        float_type = Decimal()
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_45_78_float_retorna_True(self) -> None:
        entry = 45.78
        float_type = Decimal()
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Decimal()
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Decimal(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_350_int_retorna_True(self) -> None:
        entry = 350
        float_type = Decimal(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3500_int_retorna_True(self) -> None:
        entry = 3500
        float_type = Decimal(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_35000_int_retorna_False(self) -> None:
        entry = 35000
        float_type = Decimal(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3_5_float_retorna_True(self) -> None:
        entry = 3.5
        float_type = Decimal(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3_545_float_retorna_True(self) -> None:
        entry = 3.545
        float_type = Decimal(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3_5455_float_retorna_False(self) -> None:
        entry = 3.5455
        float_type = Decimal(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Decimal(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_4000_int_retorna_True(self) -> None:
        entry = 4000
        float_type = Decimal(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_40000_int_retorna_False(self) -> None:
        entry = 40000
        float_type = Decimal(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_45_32_float_retorna_True(self) -> None:
        entry = 45.32
        float_type = Decimal(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_450_3_float_retorna_True(self) -> None:
        entry = 450.3
        float_type = Decimal(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_4_351_float_retorna_False(self) -> None:
        entry = 4.351
        float_type = Decimal(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected
