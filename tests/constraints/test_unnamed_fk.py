import pytest
from src.pysqlquery.constraints import ForeignKey
from src.pysqlquery.constraints.exceptions.unnamed_constraint import InvalidAddedColumnName
from src.pysqlquery.constraints.exceptions.unnamed_foreign_key import (
    InvalidOnDeleteClause,
    InvalidOnUpdateClause,
    InvalidRefColumn,
    InvalidRefTable,
    MissingColumnName
)
from src.pysqlquery.table import Table, Column
from src.pysqlquery.types import Integer


class TestUnnamedFk:
    def test_quando_tabela_recebe_coluna_com_ForeignKey_com_ref_table_outra_tabela_e_ref_column_id_e_acessamos_a_property_foreign_key_da_coluna_retorna_repr(self) -> None:
        class Tabela(Table):
            fk_col = Column(Integer, ForeignKey('outra_tabela', 'id'))

        entry = Tabela(test=True)
        result = str(entry.fk_col.foreign_key)
        expected = 'FOREIGN KEY (fk_col) REFERENCES OUTRA_TABELA(id)'

        assert result == expected

    def test_quando_tabela_recebe_coluna_com_ForeignKey_com_ref_table_OUTRA_TABELA_e_ref_column_ID_e_acessamos_a_property_foreign_key_da_coluna_retorna_repr(self) -> None:
        class Tabela(Table):
            fk_col = Column(Integer, ForeignKey('OUTRA_TABELA', 'ID'))

        entry = Tabela(test=True)
        result = str(entry.fk_col.foreign_key)
        expected = 'FOREIGN KEY (fk_col) REFERENCES OUTRA_TABELA(id)'

        assert result == expected

    def test_quando_tabela_recebe_coluna_com_ForeignKey_com_ref_table_outra_tabela_e_ref_column_id_e_on_delete_cascade_e_on_update_no_action_e_acessamos_a_property_foreign_key_da_coluna_retorna_repr(self) -> None:
        class Tabela(Table):
            fk_col = Column(Integer, ForeignKey('outra_tabela', 'id', on_delete='cascade', on_update='no action'))

        entry = Tabela(test=True)
        result = str(entry.fk_col.foreign_key)
        expected = 'FOREIGN KEY (fk_col) REFERENCES OUTRA_TABELA(id) ON DELETE CASCADE ON UPDATE NO ACTION'

        assert result == expected

    def test_quando_tabela_recebe_coluna_com_ForeignKey_com_ref_table_outra_tabela_e_ref_column_id_e_on_delete_cascade_e_on_update_no_action_e_acessamos_a_property_foreign_key_da_coluna_retorna_informacoes(self) -> None:
        class Tabela(Table):
            fk_col = Column(Integer, ForeignKey('outra_tabela', 'id', on_delete='cascade', on_update='no action'))

        entry = Tabela(test=True).fk_col.foreign_key

        assert entry.column == 'fk_col'
        assert entry.ref_table == 'outra_tabela'
        assert entry.ref_column == 'id'
        assert entry.on_delete == 'cascade'
        assert entry.on_update == 'no action'

    def test_quando_tabela_recebe_coluna_com_ForeignKey_com_ref_table_OUTRA_TABELA_e_ref_column_ID_e_on_delete_CASCADE_e_on_update_NO_ACTION_e_acessamos_a_property_foreign_key_da_coluna_retorna_informacoes(self) -> None:
        class Tabela(Table):
            fk_col = Column(Integer, ForeignKey('OUTRA_TABELA', 'ID', on_delete='CASCADE', on_update='NO ACTION'))

        entry = Tabela(test=True).fk_col.foreign_key

        assert entry.column == 'fk_col'
        assert entry.ref_table == 'outra_tabela'
        assert entry.ref_column == 'id'
        assert entry.on_delete == 'cascade'
        assert entry.on_update == 'no action'

    def test_quando_ref_table_recebe_str_vazia_lanca_InvalidRefTable(self) -> None:
        with pytest.raises(InvalidRefTable):
            ForeignKey('', 'id')

    def test_quando_ref_table_recebe_123_lanca_InvalidRefTable(self) -> None:
        with pytest.raises(InvalidRefTable):
            ForeignKey(123, 'id')

    def test_quando_ref_table_recebe_2teste_lanca_InvalidRefTable(self) -> None:
        with pytest.raises(InvalidRefTable):
            ForeignKey('2teste', 'id')

    def test_quando_ref_column_recebe_str_vazia_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKey('outra_coluna', '')

    def test_quando_ref_column_recebe_123_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKey('outra_coluna', 123)

    def test_quando_ref_column_recebe_2teste_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKey('outra_coluna', '2teste')

    def test_quando_on_delete_recebe_str_vazia_lanca_InvalidOnDeleteClause(self) -> None:
        with pytest.raises(InvalidOnDeleteClause):
            ForeignKey('outra_coluna', 'id', on_delete='')

    def test_quando_on_delete_recebe_123_lanca_InvalidOnDeleteClause(self) -> None:
        with pytest.raises(InvalidOnDeleteClause):
            ForeignKey('outra_coluna', 'id', on_delete=123)

    def test_quando_on_delete_recebe_2teste_lanca_InvalidOnDeleteClause(self) -> None:
        with pytest.raises(InvalidOnDeleteClause):
            ForeignKey('outra_coluna', 'id', on_delete='2teste')

    def test_quando_on_update_recebe_str_vazia_lanca_InvalidOnUpdateClause(self) -> None:
        with pytest.raises(InvalidOnUpdateClause):
            ForeignKey('outra_coluna', 'id', on_update='')

    def test_quando_on_update_recebe_123_lanca_InvalidOnUpdateClause(self) -> None:
        with pytest.raises(InvalidOnUpdateClause):
            ForeignKey('outra_coluna', 'id', on_update=123)

    def test_quando_on_update_recebe_2teste_lanca_InvalidOnUpdateClause(self) -> None:
        with pytest.raises(InvalidOnUpdateClause):
            ForeignKey('outra_coluna', 'id', on_update='2teste')

    def test_quando_esta_fora_de_tabela_e_nao_recebe_nome_de_coluna_e_convertemos_para_str_lanca_MissingColumnName(self) -> None:
        with pytest.raises(MissingColumnName):
            str(ForeignKey('outra_coluna', 'id'))

    def test_quando_adicionamos_nome_de_coluna_como_123_lanca_InvalidAddedColumnName(self) -> None:
        entry = ForeignKey('outra_coluna', 'id')

        with pytest.raises(InvalidAddedColumnName):
            entry.add_column_name(123)
