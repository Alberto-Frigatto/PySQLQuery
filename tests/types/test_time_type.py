from src.pysqlquery.types import Time


class TestTime:
    def test_quando_instanciado_retorna_TIME(self) -> None:
        entry = Time()
        expected = 'TIME'
        result = str(entry)

        assert result == expected

    def test_quando_valida_12_45_31_retorna_True(self) -> None:
        entry = '12:45:31'
        date_type = Time()
        expected = True
        result = date_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_27_02_2005_retorna_False(self) -> None:
        entry = '27-02-2005'
        date_type = Time()
        expected = False
        result = date_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_65_int_retorna_False(self) -> None:
        entry = 65
        date_type = Time()
        expected = False
        result = date_type.validate_value(entry)

        assert result == expected
