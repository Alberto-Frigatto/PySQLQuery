import pytest
from src.pysqlquery.constraints import UniqueConstraint
from src.pysqlquery.constraints.exceptions.named_constraint import (
    InvalidColumnName,
    InvalidConstraintName
)


class TestNamedUn:
    def test_quando_name_recebe_un_tabela_coluna_e_column_recebe_coluna_retorna_repr(self) -> None:
        entry = UniqueConstraint('un_tabela_coluna', 'coluna')
        result = str(entry)
        expected = 'CONSTRAINT un_tabela_coluna UNIQUE (coluna)'

        assert result == expected

    def test_quando_name_recebe_UN_TABELA_COLUNA_e_column_recebe_COLUNA_retorna_repr(self) -> None:
        entry = UniqueConstraint('UN_TABELA_COLUNA', 'COLUNA')
        result = str(entry)
        expected = 'CONSTRAINT un_tabela_coluna UNIQUE (coluna)'

        assert result == expected

    def test_quando_name_recebe_un_tabela_coluna_e_column_recebe_coluna_retorna_name_un_tabela_coluna_e_column_coluna(self) -> None:
        entry = UniqueConstraint('un_tabela_coluna', 'coluna')

        assert entry.name == 'un_tabela_coluna'
        assert entry.column == 'coluna'

    def test_quando_name_recebe_UN_TABELA_COLUNA_e_column_recebe_COLUNA_retorna_name_un_tabela_coluna_e_column_coluna(self) -> None:
        entry = UniqueConstraint('UN_TABELA_COLUNA', 'COLUNA')

        assert entry.name == 'un_tabela_coluna'
        assert entry.column == 'coluna'

    def test_quando_name_recebe_str_vazia_lanca_InvalidConstraintName(self):
        with pytest.raises(InvalidConstraintName):
            UniqueConstraint('', 'coluna')

    def test_quando_name_recebe_123_lanca_InvalidConstraintName(self):
        with pytest.raises(InvalidConstraintName):
            UniqueConstraint(123, 'coluna')

    def test_quando_name_recebe_2teste_lanca_InvalidConstraintName(self):
        with pytest.raises(InvalidConstraintName):
            UniqueConstraint('2teste', 'coluna')

    def test_quando_column_recebe_str_vazia_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            UniqueConstraint('un_constraint', '')

    def test_quando_column_recebe_123_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            UniqueConstraint('un_constraint', 123)

    def test_quando_column_recebe_2teste_lanca_InvalidColumnName(self):
        with pytest.raises(InvalidColumnName):
            UniqueConstraint('un_constraint', '2teste')
