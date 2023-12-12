from src.sqlquerybuilder.types import Date


class TestDate:
    def test_quando_instanciado_retorna_DATE(self) -> None:
        entry = Date()
        expected = 'DATE'
        result = str(entry)

        assert result == expected

    def test_quando_valida_2005_02_27_retorna_True(self) -> None:
        entry = '2005-02-27'
        date_type = Date()
        expected = True
        result = date_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_27_02_2005_retorna_False(self) -> None:
        entry = '27-02-2005'
        date_type = Date()
        expected = False
        result = date_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_65_int_retorna_False(self) -> None:
        entry = 65
        date_type = Date()
        expected = False
        result = date_type.validate_value(entry)

        assert result == expected
