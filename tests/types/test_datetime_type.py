from sqlgen.types import DateTime


class TestDateTime:
    def test_quando_instanciado_retorna_DATETIME(self) -> None:
        entry = DateTime()
        expected = 'DATETIME'
        result = str(entry)

        assert result == expected

    def test_quando_valida_2005_02_27_12_52_10_retorna_True(self) -> None:
        entry = '2005-02-27 12:52:10'
        datetime_type = DateTime()
        expected = True
        result = datetime_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_27_02_2005_retorna_False(self) -> None:
        entry = '27-02-2005 12:52:10'
        datetime_type = DateTime()
        expected = False
        result = datetime_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_65_int_retorna_False(self) -> None:
        entry = 65
        datetime_type = DateTime()
        expected = False
        result = datetime_type.validate_value(entry)

        assert result == expected
