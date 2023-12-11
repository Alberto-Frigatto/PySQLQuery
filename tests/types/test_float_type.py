import pytest
from src.sqlgen.types import Float


class TestFloat:
    def test_quando_nao_recebe_nada_retorna_FLOAT(self) -> None:
        entry = Float()
        expected = 'FLOAT'
        result = str(entry)

        assert result == expected

    def test_quando_recebe_length_4_retorna_FLOAT_4(self) -> None:
        entry = 4
        expected = 'FLOAT(4)'
        float_type = Float(entry)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_2_retorna_FLOAT_4_2(self) -> None:
        entry_length = 4
        entry_precision = 2
        expected = 'FLOAT(4, 2)'
        float_type = Float(entry_length, entry_precision)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_length_aaa_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry = 'aaa'
            Float(entry)

    def test_quando_recebe_length_0_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry = 0
            Float(entry)

    def test_quando_recebe_precision_aaa_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry = 'aaa'
            Float(precision=entry)

    def test_quando_recebe_precision_0_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry = 0
            Float(precision=entry)

    def test_quando_recebe_precision_4_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry = 4
            Float(precision=entry)

    def test_quando_recebe_length_4_e_precision_0_retorna_FLOAT_4_0(self) -> None:
        entry_length = 4
        entry_precision = 0
        expected = 'FLOAT(4, 0)'
        float_type = Float(entry_length, entry_precision)
        result = str(float_type)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_4_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry_length = 4
            entry_precision = 4
            Float(entry_length, entry_precision)

    def test_quando_recebe_length_4_e_precision_aaa_lanca_exception(self) -> None:
        with pytest.raises(Exception):
            entry_length = 4
            entry_precision = 'aaa'
            Float(entry_length, entry_precision)

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

    def test_quando_recebe_length_4_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Float(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_valida_350_int_retorna_True(self) -> None:
        entry = 350
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_valida_3500_int_retorna_True(self) -> None:
        entry = 3500
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_valida_35000_int_retorna_False(self) -> None:
        entry = 35000
        float_type = Float(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_valida_3_5_float_retorna_True(self) -> None:
        entry = 3.5
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_valida_3_545_float_retorna_True(self) -> None:
        entry = 3.545
        float_type = Float(4)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_valida_3_5455_float_retorna_False(self) -> None:
        entry = 3.5455
        float_type = Float(4)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_2_e_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        float_type = Float(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_2_e_valida_4000_int_retorna_True(self) -> None:
        entry = 4000
        float_type = Float(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_2_e_valida_40000_int_retorna_False(self) -> None:
        entry = 40000
        float_type = Float(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_2_e_valida_45_32_float_retorna_True(self) -> None:
        entry = 45.32
        float_type = Float(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_2_e_valida_450_3_float_retorna_True(self) -> None:
        entry = 450.3
        float_type = Float(4, 2)
        expected = True
        result = float_type.validate_value(entry)

        assert result == expected

    def test_quando_recebe_length_4_e_precision_2_e_valida_4_351_float_retorna_False(self) -> None:
        entry = 4.351
        float_type = Float(4, 2)
        expected = False
        result = float_type.validate_value(entry)

        assert result == expected
