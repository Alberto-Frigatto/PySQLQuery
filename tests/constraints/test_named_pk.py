import pytest
from src.pysqlquery.constraints import PrimaryKeyConstraint
from src.pysqlquery.constraints.exceptions.named_constraint import (
    InvalidColumnName,
    InvalidConstraintName
)
from src.pysqlquery.constraints.exceptions.multi_column_named_constraint import InvalidColumnType


class TestNamedPk:
    def test_quando_name_recebe_pk_tabela_e_column_recebe_id_retorna_repr(self) -> None:
        entry = PrimaryKeyConstraint('pk_tabela', 'id')
        result = str(entry)
        expected = 'CONSTRAINT pk_tabela PRIMARY KEY (id)'

        assert result == expected

    def test_quando_name_recebe_PK_TABELA_e_column_recebe_ID_retorna_repr(self) -> None:
        entry = PrimaryKeyConstraint('PK_TABELA', 'ID')
        result = str(entry)
        expected = 'CONSTRAINT pk_tabela PRIMARY KEY (id)'

        assert result == expected

    def test_quando_name_recebe_pk_tabela_e_column_recebe_id_como_lista_retorna_repr(self) -> None:
        entry = PrimaryKeyConstraint('pk_tabela', ['id'])
        result = str(entry)
        expected = 'CONSTRAINT pk_tabela PRIMARY KEY (id)'

        assert result == expected

    def test_quando_name_recebe_pk_tabela_e_column_recebe_id_e_cpf_retorna_repr(self) -> None:
        entry = PrimaryKeyConstraint('pk_tabela', ['id', 'cpf'])
        result = str(entry)
        expected = 'CONSTRAINT pk_tabela PRIMARY KEY (id, cpf)'

        assert result == expected

    def test_quando_name_recebe_PK_TABELA_e_column_recebe_ID_e_CPF_retorna_repr(self) -> None:
        entry = PrimaryKeyConstraint('PK_TABELA', ['ID', 'CPF'])
        result = str(entry)
        expected = 'CONSTRAINT pk_tabela PRIMARY KEY (id, cpf)'

        assert result == expected

    def test_quando_name_recebe_pk_tabela_e_column_recebe_id_retorna_name_pk_tabela_e_column_id(self) -> None:
        entry = PrimaryKeyConstraint('pk_tabela', 'id')

        assert entry.name == 'pk_tabela'
        assert entry.column == 'id'

    def test_quando_name_recebe_PK_TABELA_e_column_recebe_ID_retorna_name_pk_tabela_e_column_id(self) -> None:
        entry = PrimaryKeyConstraint('PK_TABELA', 'ID')

        assert entry.name == 'pk_tabela'
        assert entry.column == 'id'

    def test_quando_name_recebe_pk_tabela_e_column_recebe_id_como_lista_retorna_name_pk_tabela_e_column_id_como_str(self) -> None:
        entry = PrimaryKeyConstraint('pk_tabela', ['id'])

        assert entry.name == 'pk_tabela'
        assert entry.column == 'id'

    def test_quando_name_recebe_pk_tabela_e_column_recebe_id_e_cpf_retorna_name_pk_tabela_e_column_id_e_cpf(self) -> None:
        entry = PrimaryKeyConstraint('pk_tabela', ['id', 'cpf'])

        assert entry.name == 'pk_tabela'
        assert entry.column == ['id', 'cpf']

    def test_quando_name_recebe_PK_TABELA_e_column_recebe_ID_e_CPF_retorna_name_pk_tabela_e_column_id_e_cpf(self) -> None:
        entry = PrimaryKeyConstraint('PK_TABELA', ['ID', 'CPF'])

        assert entry.name == 'pk_tabela'
        assert entry.column == ['id', 'cpf']

    def test_quando_name_recebe_str_vazia_lanca_InvalidConstraintName(self):
        with pytest.raises(InvalidConstraintName):
            PrimaryKeyConstraint('', 'coluna')

    def test_quando_name_recebe_123_lanca_InvalidConstraintName(self):
        with pytest.raises(InvalidConstraintName):
            PrimaryKeyConstraint(123, 'coluna')

    def test_quando_name_recebe_2teste_lanca_InvalidConstraintName(self):
        with pytest.raises(InvalidConstraintName):
            PrimaryKeyConstraint('2teste', 'coluna')

    def test_quando_column_recebe_123_lanca_InvalidColumnType(self):
        with pytest.raises(InvalidColumnType):
            PrimaryKeyConstraint('pk_constraint', 123)

    def test_quando_column_recebe_str_vazia_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            PrimaryKeyConstraint('pk_constraint', '')

    def test_quando_column_recebe_2teste_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            PrimaryKeyConstraint('pk_constraint', '2teste')

    def test_quando_column_recebe_id_e_str_vazia_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            PrimaryKeyConstraint('pk_constraint', ['id', ''])

    def test_quando_column_recebe_id_e_123_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            PrimaryKeyConstraint('pk_constraint', ['id', 123])

    def test_quando_column_recebe_id_e_2teste_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            PrimaryKeyConstraint('pk_constraint', ['id', '2teste'])
