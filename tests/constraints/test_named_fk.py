import pytest
from src.pysqlquery.constraints import ForeignKeyConstraint
from src.pysqlquery.constraints.exceptions.multi_column_named_constraint import InvalidColumnType
from src.pysqlquery.constraints.exceptions.named_constraint import (
    InvalidColumnName,
    InvalidConstraintName
)
from src.pysqlquery.constraints.exceptions.named_foreign_key import (
    InvalidOnDeleteClause,
    InvalidOnUpdateClause,
    InvalidRefColumn,
    InvalidRefColumnListLength,
    InvalidRefColumnType,
    InvalidRefTable,
    RefColumnMustBeList,
    RefColumnMustBeStr
)


class TestNamedFk:
    def test_quando_recebe_name_fk_tabela_outra_tabela_e_column_fk_col_e_ref_table_outra_tabela_e_ref_column_id_retorna_repr(self) -> None:
        entry = ForeignKeyConstraint('fk_tabela_outra_tabela', 'fk_col', 'outra_tabela', 'id')
        result = str(entry)
        expected = 'CONSTRAINT fk_tabela_outra_tabela FOREIGN KEY (fk_col) REFERENCES OUTRA_TABELA(id)'

        assert result == expected

    def test_quando_recebe_name_FK_TABELA_OUTRA_TABELA_e_column_FK_COL_e_ref_table_OUTRA_TABELA_e_ref_column_ID_retorna_repr(self) -> None:
        entry = ForeignKeyConstraint('FK_TABELA_OUTRA_TABELA', 'FK_COL', 'OUTRA_TABELA', 'ID')
        result = str(entry)
        expected = 'CONSTRAINT fk_tabela_outra_tabela FOREIGN KEY (fk_col) REFERENCES OUTRA_TABELA(id)'

        assert result == expected

    def test_quando_recebe_name_fk_tabela_outra_tabela_e_column_fk_col_e_ref_table_outra_tabela_e_ref_column_id_e_on_delete_cascade_e_on_update_no_action_retorna_repr(self) -> None:
        entry = ForeignKeyConstraint('fk_tabela_outra_tabela', 'fk_col', 'outra_tabela', 'id', on_delete='cascade', on_update='no action')
        result = str(entry)
        expected = 'CONSTRAINT fk_tabela_outra_tabela FOREIGN KEY (fk_col) REFERENCES OUTRA_TABELA(id) ON DELETE CASCADE ON UPDATE NO ACTION'

        assert result == expected

    def test_quando_recebe_name_fk_tabela_outra_tabela_e_column_fk_col_e_ref_table_outra_tabela_e_ref_column_id_retorna_informacoes(self) -> None:
        entry = ForeignKeyConstraint('fk_tabela_outra_tabela', 'fk_col', 'outra_tabela', 'id')

        assert entry.name == 'fk_tabela_outra_tabela'
        assert entry.column == 'fk_col'
        assert entry.ref_table == 'outra_tabela'
        assert entry.ref_column == 'id'
        assert entry.on_delete == None
        assert entry.on_update == None

    def test_quando_recebe_name_FK_TABELA_OUTRA_TABELA_e_column_FK_COL_e_ref_table_OUTRA_TABELA_e_ref_column_ID_e_on_delete_CASCADE_e_on_update_NO_ACTION_retorna_informacoes(self) -> None:
        entry = ForeignKeyConstraint('FK_TABELA_OUTRA_TABELA', 'FK_COL', 'OUTRA_TABELA', 'ID', on_delete='CASCADE', on_update='NO ACTION')

        assert entry.name == 'fk_tabela_outra_tabela'
        assert entry.column == 'fk_col'
        assert entry.ref_table == 'outra_tabela'
        assert entry.ref_column == 'id'
        assert entry.on_delete == 'cascade'
        assert entry.on_update == 'no action'

    def test_quando_recebe_name_fk_tabela_outra_tabela_e_column_fk_col_1_e_fk_col_2_e_ref_table_outra_tabela_e_ref_column_id_1_e_id_2_e_on_delete_cascade_e_on_update_no_action_retorna_repr(self) -> None:
        entry = ForeignKeyConstraint('fk_tabela_outra_tabela', ['fk_col_1', 'fk_col_2'], 'outra_tabela', ['id_1', 'id_2'], on_delete='cascade', on_update='no action')
        result = str(entry)
        expected = 'CONSTRAINT fk_tabela_outra_tabela FOREIGN KEY (fk_col_1, fk_col_2) REFERENCES OUTRA_TABELA(id_1, id_2) ON DELETE CASCADE ON UPDATE NO ACTION'

        assert result == expected

    def test_quando_recebe_name_fk_tabela_outra_tabela_e_column_fk_col_1_e_fk_col_2_e_ref_table_outra_tabela_e_ref_column_id_1_e_id_2_e_on_delete_cascade_e_on_update_no_action_retorna_informacoes(self) -> None:
        entry = ForeignKeyConstraint('fk_tabela_outra_tabela', ['fk_col_1', 'fk_col_2'], 'outra_tabela', ['id_1', 'id_2'], on_delete='cascade', on_update='no action')

        assert entry.name == 'fk_tabela_outra_tabela'
        assert entry.column == ['fk_col_1', 'fk_col_2']
        assert entry.ref_table == 'outra_tabela'
        assert entry.ref_column == ['id_1', 'id_2']
        assert entry.on_delete == 'cascade'
        assert entry.on_update == 'no action'

    def test_quando_name_recebe_str_vazia_lanca_InvalidConstraintName(self) -> None:
        with pytest.raises(InvalidConstraintName):
            ForeignKeyConstraint('', 'fk_col', 'outra_tabela', 'id')

    def test_quando_name_recebe_123_lanca_InvalidConstraintName(self) -> None:
        with pytest.raises(InvalidConstraintName):
            ForeignKeyConstraint(123, 'fk_col', 'outra_tabela', 'id')

    def test_quando_name_recebe_2teste_lanca_InvalidConstraintName(self) -> None:
        with pytest.raises(InvalidConstraintName):
            ForeignKeyConstraint('2teste', 'fk_col', 'outra_tabela', 'id')

    def test_quando_column_recebe_123_lanca_InvalidColumnType(self) -> None:
        with pytest.raises(InvalidColumnType):
            ForeignKeyConstraint('fk_constraint', 123, 'outra_tabela', 'id')

    def test_quando_column_recebe_str_vazia_lanca_InvalidColumnName(self) -> None:
        with pytest.raises(InvalidColumnName):
            ForeignKeyConstraint('fk_constraint', '', 'outra_tabela', 'id')

    def test_quando_column_recebe_2teste_lanca_InvalidColumnName(self) -> None:
        with pytest.raises(InvalidColumnName):
            ForeignKeyConstraint('fk_constraint', '2teste', 'outra_tabela', 'id')

    def test_quando_column_recebe_id_e_str_vazia_lanca_InvalidColumnName(self) -> None:
        with pytest.raises(InvalidColumnName):
            ForeignKeyConstraint('fk_constraint', ['id', ''], 'outra_tabela', 'id')

    def test_quando_column_recebe_id_e_2teste_lanca_InvalidColumnName(self) -> None:
        with pytest.raises(InvalidColumnName):
            ForeignKeyConstraint('fk_constraint', ['id', '2teste'], 'outra_tabela', 'id')

    def test_quando_on_delete_recebe_123_lanca_InvalidOnDeleteClause(self) -> None:
        with pytest.raises(InvalidOnDeleteClause):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabela', 'id', on_delete=123)

    def test_quando_on_delete_recebe_str_vazia_lanca_InvalidOnDeleteClause(self) -> None:
        with pytest.raises(InvalidOnDeleteClause):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabela', 'id', on_delete='')

    def test_quando_on_delete_recebe_2teste_lanca_InvalidOnDeleteClause(self) -> None:
        with pytest.raises(InvalidOnDeleteClause):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabela', 'id', on_delete='2teste')

    def test_quando_on_update_recebe_123_lanca_InvalidOnUpdateClause(self) -> None:
        with pytest.raises(InvalidOnUpdateClause):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabela', 'id', on_update=123)

    def test_quando_on_update_recebe_str_vazia_lanca_InvalidOnUpdateClause(self) -> None:
        with pytest.raises(InvalidOnUpdateClause):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabela', 'id', on_update='')

    def test_quando_on_update_recebe_2teste_lanca_InvalidOnUpdateClause(self) -> None:
        with pytest.raises(InvalidOnUpdateClause):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabela', 'id', on_update='2teste')

    def test_quando_ref_table_recebe_str_vazia_lanca_InvalidRefTable(self) -> None:
        with pytest.raises(InvalidRefTable):
            ForeignKeyConstraint('fk_constraint', 'fk_col', '', 'id')

    def test_quando_ref_table_recebe_123_lanca_InvalidRefTable(self) -> None:
        with pytest.raises(InvalidRefTable):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 123, 'id')

    def test_quando_ref_table_recebe_2teste_lanca_InvalidRefTable(self) -> None:
        with pytest.raises(InvalidRefTable):
            ForeignKeyConstraint('fk_constraint', 'fk_col', '2teste', 'id')

    def test_quando_ref_column_recebe_123_lanca_InvalidRefColumnType(self) -> None:
        with pytest.raises(InvalidRefColumnType):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabala', 123)

    def test_quando_ref_column_recebe_str_vazia_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabala', '')

    def test_quando_ref_column_recebe_2teste_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabala', '2teste')

    def test_quando_column_recebe_fk_col_1_e_fk_col_2_e_ref_column_recebe_id_e_123_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKeyConstraint('fk_constraint', ['fk_col_1', 'fk_col_2'], 'outra_tabala', ['id', 123])

    def test_quando_column_recebe_fk_col_1_e_fk_col_2_e_ref_column_recebe_id_e_str_vazia_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKeyConstraint('fk_constraint', ['fk_col_1', 'fk_col_2'], 'outra_tabala', ['id', ''])

    def test_quando_column_recebe_fk_col_1_e_fk_col_2_e_ref_column_recebe_id_e_2teste_lanca_InvalidRefColumn(self) -> None:
        with pytest.raises(InvalidRefColumn):
            ForeignKeyConstraint('fk_constraint', ['fk_col_1', 'fk_col_2'], 'outra_tabala', ['id', '2teste'])

    def test_quando_column_recebe_list_e_ref_column_recebe_str_lanca_RefColumnMustBeList(self) -> None:
        with pytest.raises(RefColumnMustBeList):
            ForeignKeyConstraint('fk_constraint', ['fk_col_1', 'fk_col_2'], 'outra_tabala', 'id')

    def test_quando_column_recebe_str_e_ref_column_recebe_list_lanca_RefColumnMustBeStr(self) -> None:
        with pytest.raises(RefColumnMustBeStr):
            ForeignKeyConstraint('fk_constraint', 'fk_col', 'outra_tabala', ['id_1', 'id_2'])

    def test_quando_column_recebe_list_com_2_colunas_e_ref_column_recebe_list_com_3_colunas_lanca_InvalidRefColumnListLength(self) -> None:
        with pytest.raises(InvalidRefColumnListLength):
            ForeignKeyConstraint('fk_constraint', ['fk_col_1', 'fk_col_2'], 'outra_tabala', ['id_1', 'id_2', 'id_3'])
