from src.pysqlquery.types import Boolean


class TestBoolean:
    def test_quando_instanciado_retorna_BOOLEAN(self) -> None:
        entry = Boolean()
        expected = 'BOOLEAN'
        result = str(entry)

        assert result == expected

    def test_quando_valida_True_int_retorna_True(self) -> None:
        entry = True
        int_type = Boolean()
        expected = True
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_False_int_retorna_True(self) -> None:
        entry = False
        int_type = Boolean()
        expected = True
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_0_int_retorna_False(self) -> None:
        entry = 0
        int_type = Boolean()
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_1_int_retorna_False(self) -> None:
        entry = 1
        int_type = Boolean()
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_6e7_int_retorna_False(self) -> None:
        entry = int(6e7)
        int_type = Boolean()
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected

    def test_quando_valida_alberto_retorna_False(self) -> None:
        entry = 'alberto'
        int_type = Boolean()
        expected = False
        result = int_type.validate_value(entry)

        assert result == expected

