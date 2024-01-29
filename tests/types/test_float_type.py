import pytest

from src.pysqlquery.types import Float
from src.pysqlquery.types.exceptions.sql_decimal_type import InvalidScale
from src.pysqlquery.types.exceptions.sql_num_type import InvalidPrecision


class TestFloat:
    def test_quando_nao_recebe_nada_retorna_FLOAT(self) -> None:
        entry = Float()
        expected = 'FLOAT'
        result = str(entry)

        assert result == expected

    def test_quando_recebe_precision_4_retorna_FLOAT_4(self) -> None:
        entry = 4
        expected = 'FLOAT(4)'
        float_type = Float(entry)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_retorna_FLOAT_4_2(self) -> None:
        entry_precision = 4
        entry_scale = 2
        expected = 'FLOAT(4, 2)'
        float_type = Float(entry_precision, entry_scale)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_precision_aaa_lanca_InvalidPrecision(self) -> None:
        with pytest.raises(InvalidPrecision):
            entry = 'aaa'
            Float(entry)

    def test_quando_recebe_precision_0_lanca_InvalidPrecision(self) -> None:
        with pytest.raises(InvalidPrecision):
            entry = 0
            Float(entry)

    def test_quando_recebe_scale_aaa_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry = 'aaa'
            Float(scale=entry)

    def test_quando_recebe_scale_0_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry = 0
            Float(scale=entry)

    def test_quando_recebe_scale_4_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry = 4
            Float(scale=entry)

    def test_quando_recebe_precision_4_e_scale_0_retorna_FLOAT_4_0(self) -> None:
        entry_precision = 4
        entry_scale = 0
        expected = 'FLOAT(4, 0)'
        float_type = Float(entry_precision, entry_scale)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_4_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry_precision = 4
            entry_scale = 4
            Float(entry_precision, entry_scale)

    def test_quando_recebe_precision_4_e_scale_aaa_lanca_InvalidScale(self) -> None:
        with pytest.raises(InvalidScale):
            entry_precision = 4
            entry_scale = 'aaa'
            Float(entry_precision, entry_scale)

    def test_quando_nao_recebe_nada_e_valida_6e7_int_retorna_True(self) -> None:
        entry = int(6e7)
        float_type = Float()
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_45_78_float_retorna_True(self) -> None:
        entry = 45.78
        float_type = Float()
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_nao_recebe_nada_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Float()
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Float(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_350_int_retorna_True(self) -> None:
        entry = 350
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3500_int_retorna_True(self) -> None:
        entry = 3500
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_35000_int_retorna_False(self) -> None:
        entry = 35000
        float_type = Float(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3_5_float_retorna_True(self) -> None:
        entry = 3.5
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3_545_float_retorna_True(self) -> None:
        entry = 3.545
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_valida_3_5455_float_retorna_False(self) -> None:
        entry = 3.5455
        float_type = Float(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Float(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_4000_int_retorna_True(self) -> None:
        entry = 4000
        float_type = Float(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_40000_int_retorna_False(self) -> None:
        entry = 40000
        float_type = Float(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_45_32_float_retorna_True(self) -> None:
        entry = 45.32
        float_type = Float(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_450_3_float_retorna_True(self) -> None:
        entry = 450.3
        float_type = Float(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_precision_4_e_scale_2_e_valida_4_351_float_retorna_False(self) -> None:
        entry = 4.351
        float_type = Float(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected
