import pytest
from pysqlquery.constraints.named import primary_key
from src.pysqlquery.table import Table, Column
from src.pysqlquery.constraints import (
    ForeignKey,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint
)
from src.pysqlquery.types import Integer, Char, String, Float
from src.pysqlquery.table.exceptions.table import (
    InvalidConstraintList,
    InvalidNamedConstraint,
    InvalidName,
    InvalidTestValue,
    MultiplePrimaryKeyConstraints,
    InvalidCreateIfNotExistsValue
)


class TestTable:
    def test_quando_test_recebe_True_a_tabela_nao_e_incluida_na_lista_global_de_tabelas(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        entry = Tabela(test=True)

        assert entry not in Table.all_tables

    def test_quando_test_recebe_True_e_acessamos_a_property_test_retorna_True(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        entry = Tabela(test=True)
        result = entry.test
        expected = True

        assert result == expected

    def test_quando_nao_recebe__tablename__e_recebe_colunas_id_nome_sobrenome_cpf_salario_id_setor_com_unnamed_constraints_retorna_repr(self) -> None:
        class Tabela(Table):
            id = Column(Integer, primary_key=True, auto_increment='mysql')
            nome = Column(String(50))
            sobrenome = Column(String, nullable=True)
            cpf = Column(Char(11), unique=True)
            salario = Column(Float(7, 2), default=1212.78)
            id_setor = Column(Integer, ForeignKey('t_setor', 'id'))

        entry = Tabela(test=True)
        result = str(entry)
        expected = 'CREATE TABLE TABELA (\n\tid INTEGER AUTO_INCREMENT NOT NULL,\n\tnome VARCHAR(50) NOT NULL,\n\tsobrenome VARCHAR,\n\tcpf CHAR(11) NOT NULL UNIQUE,\n\tsalario FLOAT(7, 2) NOT NULL DEFAULT 1212.78,\n\tid_setor INTEGER NOT NULL,\n\n\tPRIMARY KEY (id),\n\tFOREIGN KEY (id_setor) REFERENCES T_SETOR(id)\n);'

        assert result == expected

    def test_quando_recebe__tablename__t_funcionario_e_recebe_colunas_id_nome_sobrenome_cpf_salario_id_setor_com_unnamed_constraints_retorna_repr(self) -> None:
        class Tabela(Table):
            __tablename__ = 't_funcionario'

            id = Column(Integer, primary_key=True, auto_increment='mysql')
            nome = Column(String(50))
            sobrenome = Column(String, nullable=True)
            cpf = Column(Char(11), unique=True)
            salario = Column(Float(7, 2), default=1212.78)
            id_setor = Column(Integer, ForeignKey('t_setor', 'id'))

        entry = Tabela(test=True)
        result = str(entry)
        expected = 'CREATE TABLE T_FUNCIONARIO (\n\tid INTEGER AUTO_INCREMENT NOT NULL,\n\tnome VARCHAR(50) NOT NULL,\n\tsobrenome VARCHAR,\n\tcpf CHAR(11) NOT NULL UNIQUE,\n\tsalario FLOAT(7, 2) NOT NULL DEFAULT 1212.78,\n\tid_setor INTEGER NOT NULL,\n\n\tPRIMARY KEY (id),\n\tFOREIGN KEY (id_setor) REFERENCES T_SETOR(id)\n);'

        assert result == expected

    def test_quando_recebe__tablename__T_FUNCIONARIO_e_recebe_colunas_id_nome_sobrenome_cpf_salario_id_setor_com_unnamed_constraints_retorna_repr(self) -> None:
        class Tabela(Table):
            __tablename__ = 'T_FUNCIONARIO'

            id = Column(Integer, primary_key=True, auto_increment='mysql')
            nome = Column(String(50))
            sobrenome = Column(String, nullable=True)
            cpf = Column(Char(11), unique=True)
            salario = Column(Float(7, 2), default=1212.78)
            id_setor = Column(Integer, ForeignKey('t_setor', 'id'))

        entry = Tabela(test=True)
        result = str(entry)
        expected = 'CREATE TABLE T_FUNCIONARIO (\n\tid INTEGER AUTO_INCREMENT NOT NULL,\n\tnome VARCHAR(50) NOT NULL,\n\tsobrenome VARCHAR,\n\tcpf CHAR(11) NOT NULL UNIQUE,\n\tsalario FLOAT(7, 2) NOT NULL DEFAULT 1212.78,\n\tid_setor INTEGER NOT NULL,\n\n\tPRIMARY KEY (id),\n\tFOREIGN KEY (id_setor) REFERENCES T_SETOR(id)\n);'

        assert result == expected

    def test_quando_recebe__tablename__t_funcionario_e_recebe_colunas_id_nome_sobrenome_cpf_salario_id_setor_com_named_constraints_retorna_repr(self) -> None:
        class Tabela(Table):
            __tablename__ = 't_funcionario'

            id = Column(Integer, auto_increment='mysql')
            nome = Column(String(50))
            sobrenome = Column(String, nullable=True)
            cpf = Column(Char(11))
            salario = Column(Float(7, 2), default=1212.78)
            id_setor = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'id'),
                UniqueConstraint('un_tabela_cpf', 'cpf'),
                ForeignKeyConstraint('fk_funcionario_setor', 'id_setor', 't_setor', 'id')
            ]

        entry = Tabela(test=True)
        result = str(entry)
        expected = 'CREATE TABLE T_FUNCIONARIO (\n\tid INTEGER AUTO_INCREMENT NOT NULL,\n\tnome VARCHAR(50) NOT NULL,\n\tsobrenome VARCHAR,\n\tcpf CHAR(11) NOT NULL,\n\tsalario FLOAT(7, 2) NOT NULL DEFAULT 1212.78,\n\tid_setor INTEGER NOT NULL\n);\n\nALTER TABLE T_FUNCIONARIO\n\tADD CONSTRAINT pk_tabela PRIMARY KEY (id);\n\nALTER TABLE T_FUNCIONARIO\n\tADD CONSTRAINT un_tabela_cpf UNIQUE (cpf);\n\nALTER TABLE T_FUNCIONARIO\n\tADD CONSTRAINT fk_funcionario_setor FOREIGN KEY (id_setor) REFERENCES T_SETOR(id);'

        assert result == expected

    def test_quando_create_if_not_exists_recebe_True_retorna_repr_com_IF_NOT_EXISTS(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        entry = Tabela(create_if_not_exists=True, test=True)
        result = str(entry)
        expected = 'CREATE TABLE IF NOT EXISTS TABELA (\n\tcol INTEGER NOT NULL\n);'

        assert result == expected

    def test_quando_nao_recebe__tablename__e_acessamos_a_property_table_name_retorna_o_nome_da_classe_em_maiusculo(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        entry = Tabela(test=True)
        result = entry.tablename
        expected = entry.__class__.__name__.upper()

        assert result == expected

    def test_quando_recebe_1_coluna_com_unnamed_pk_e_acessamos_a_property_primary_key_retorna_essa_coluna(self) -> None:
        class Tabela(Table):
            pk_col = Column(Integer, primary_key=True)

        entry = Tabela(test=True)
        result = entry.primary_key

        assert entry.pk_col in result

    def test_quando_recebe_2_colunas_com_unnamed_pk_e_acessamos_a_property_primary_key_retorna_as_duas_colunas(self) -> None:
        class Tabela(Table):
            pk_col_1 = Column(Integer, primary_key=True)
            pk_col_2 = Column(Integer, primary_key=True)

        entry = Tabela(test=True)
        result = entry.primary_key

        assert entry.pk_col_1 in result
        assert entry.pk_col_2 in result

    def test_quando_recebe_1_coluna_com_named_pk_e_acessamos_a_property_primary_key_retorna_essa_coluna(self) -> None:
        class Tabela(Table):
            pk_col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'pk_col')
            ]

        entry = Tabela(test=True)
        result = entry.primary_key

        assert entry.pk_col in result

    def test_quando_recebe_2_colunas_com_named_pk_e_acessamos_a_property_primary_key_retorna_as_duas_colunas(self) -> None:
        class Tabela(Table):
            pk_col_1 = Column(Integer)
            pk_col_2 = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', ['pk_col_1', 'pk_col_2'])
            ]

        entry = Tabela(test=True)
        result = entry.primary_key

        assert entry.pk_col_1 in result
        assert entry.pk_col_2 in result

    def test_quando_recebe_3_named_constraints_e_acessamos_a_property_named_constraints_retorna_informacoes(self) -> None:
        class Tabela(Table):
            pk_col = Column(Integer)
            fk_col = Column(Integer)
            un_col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'pk_col'),
                UniqueConstraint('un_tabela', 'un_col'),
                ForeignKeyConstraint('fk_tabela', 'fk_col', 'outra_tabela', 'id')
            ]

        entry = Tabela(test=True).named_constraints

        assert isinstance(entry[0], PrimaryKeyConstraint)
        assert isinstance(entry[1], UniqueConstraint)
        assert isinstance(entry[2], ForeignKeyConstraint)
        assert entry[0].name == 'pk_tabela'
        assert entry[1].name == 'un_tabela'
        assert entry[2].name == 'fk_tabela'
        assert entry[0].column == 'pk_col'
        assert entry[1].column == 'un_col'
        assert entry[2].column == 'fk_col'

    def test_quando_nao_recebe__tablename__e_recebe_colunas_id_nome_sobrenome_cpf_salario_id_setor_com_unnamed_constraints_e_acessamos_a_property_columns_retorna_informacoes(self) -> None:
        class Tabela(Table):
            id = Column(Integer, primary_key=True, auto_increment='mysql')
            nome = Column(String(50))
            sobrenome = Column(String, nullable=True)
            cpf = Column(Char(11), unique=True)
            salario = Column(Float(7, 2), default=1212.78)
            id_setor = Column(Integer, ForeignKey('t_setor', 'id'))

        entry = Tabela(test=True).columns

        assert str(entry[0]) == 'id INTEGER AUTO_INCREMENT NOT NULL'
        assert str(entry[1]) == 'nome VARCHAR(50) NOT NULL'
        assert str(entry[2]) == 'sobrenome VARCHAR'
        assert str(entry[3]) == 'cpf CHAR(11) NOT NULL UNIQUE'
        assert str(entry[4]) == 'salario FLOAT(7, 2) NOT NULL DEFAULT 1212.78'
        assert str(entry[5]) == 'id_setor INTEGER NOT NULL'
        assert str(entry[0].data_type) == 'INTEGER'
        assert str(entry[1].data_type) == 'VARCHAR(50)'
        assert str(entry[2].data_type) == 'VARCHAR'
        assert str(entry[3].data_type) == 'CHAR(11)'
        assert str(entry[4].data_type) == 'FLOAT(7, 2)'
        assert str(entry[5].data_type) == 'INTEGER'
        assert isinstance(entry[0].data_type, Integer)
        assert isinstance(entry[1].data_type, String)
        assert isinstance(entry[2].data_type, String)
        assert isinstance(entry[3].data_type, Char)
        assert isinstance(entry[4].data_type, Float)
        assert isinstance(entry[5].data_type, Integer)
        assert entry[0].primary_key
        assert not entry[1].primary_key
        assert not entry[2].primary_key
        assert not entry[3].primary_key
        assert not entry[4].primary_key
        assert not entry[5].primary_key
        assert entry[0].auto_increment
        assert not entry[1].auto_increment
        assert not entry[2].auto_increment
        assert not entry[3].auto_increment
        assert not entry[4].auto_increment
        assert not entry[5].auto_increment
        assert entry[0].name == 'id'
        assert entry[1].name == 'nome'
        assert entry[2].name == 'sobrenome'
        assert entry[3].name == 'cpf'
        assert entry[4].name == 'salario'
        assert entry[5].name == 'id_setor'
        assert not entry[0].nullable
        assert not entry[1].nullable
        assert entry[2].nullable
        assert not entry[3].nullable
        assert not entry[4].nullable
        assert not entry[5].nullable
        assert entry[0].unique
        assert not entry[1].unique
        assert not entry[2].unique
        assert entry[3].unique
        assert not entry[4].unique
        assert not entry[5].unique
        assert entry[0].default is None
        assert entry[1].default is None
        assert entry[2].default is None
        assert entry[3].default is None
        assert entry[4].default == 1212.78
        assert entry[5].default is None
        assert entry[0].foreign_key is None
        assert entry[1].foreign_key is None
        assert entry[2].foreign_key is None
        assert entry[3].foreign_key is None
        assert entry[4].foreign_key is None
        assert entry[5].foreign_key is not None
        assert isinstance(entry[5].foreign_key, ForeignKey)

    def test_quando_nao_recebe__tablename__e_recebe_colunas_id_nome_sobrenome_cpf_salario_id_setor_com_named_constraints_e_acessamos_a_property_columns_retorna_informacoes(self) -> None:
        class Tabela(Table):
            id = Column(Integer, auto_increment='mysql')
            nome = Column(String(50))
            sobrenome = Column(String, nullable=True)
            cpf = Column(Char(11))
            salario = Column(Float(7, 2), default=1212.78)
            id_setor = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'id'),
                UniqueConstraint('un_tabela_cpf', 'cpf'),
                ForeignKeyConstraint('fk_tabela_setor', 'id_setor', 't_setor', 'id')
            ]

        entry = Tabela(test=True).columns

        assert str(entry[0]) == 'id INTEGER AUTO_INCREMENT NOT NULL'
        assert str(entry[1]) == 'nome VARCHAR(50) NOT NULL'
        assert str(entry[2]) == 'sobrenome VARCHAR'
        assert str(entry[3]) == 'cpf CHAR(11) NOT NULL'
        assert str(entry[4]) == 'salario FLOAT(7, 2) NOT NULL DEFAULT 1212.78'
        assert str(entry[5]) == 'id_setor INTEGER NOT NULL'
        assert str(entry[0].data_type) == 'INTEGER'
        assert str(entry[1].data_type) == 'VARCHAR(50)'
        assert str(entry[2].data_type) == 'VARCHAR'
        assert str(entry[3].data_type) == 'CHAR(11)'
        assert str(entry[4].data_type) == 'FLOAT(7, 2)'
        assert str(entry[5].data_type) == 'INTEGER'
        assert isinstance(entry[0].data_type, Integer)
        assert isinstance(entry[1].data_type, String)
        assert isinstance(entry[2].data_type, String)
        assert isinstance(entry[3].data_type, Char)
        assert isinstance(entry[4].data_type, Float)
        assert isinstance(entry[5].data_type, Integer)
        assert entry[0].primary_key
        assert not entry[1].primary_key
        assert not entry[2].primary_key
        assert not entry[3].primary_key
        assert not entry[4].primary_key
        assert not entry[5].primary_key
        assert entry[0].auto_increment
        assert not entry[1].auto_increment
        assert not entry[2].auto_increment
        assert not entry[3].auto_increment
        assert not entry[4].auto_increment
        assert not entry[5].auto_increment
        assert entry[0].name == 'id'
        assert entry[1].name == 'nome'
        assert entry[2].name == 'sobrenome'
        assert entry[3].name == 'cpf'
        assert entry[4].name == 'salario'
        assert entry[5].name == 'id_setor'
        assert not entry[0].nullable
        assert not entry[1].nullable
        assert entry[2].nullable
        assert not entry[3].nullable
        assert not entry[4].nullable
        assert not entry[5].nullable
        assert entry[0].unique
        assert not entry[1].unique
        assert not entry[2].unique
        assert entry[3].unique
        assert not entry[4].unique
        assert not entry[5].unique
        assert entry[0].default is None
        assert entry[1].default is None
        assert entry[2].default is None
        assert entry[3].default is None
        assert entry[4].default == 1212.78
        assert entry[5].default is None
        assert entry[0].foreign_key is None
        assert entry[1].foreign_key is None
        assert entry[2].foreign_key is None
        assert entry[3].foreign_key is None
        assert entry[4].foreign_key is None
        assert entry[5].foreign_key is not None
        assert isinstance(entry[5].foreign_key, ForeignKeyConstraint)

    def test_quando__tablename__recebe_str_vazia_lanca_InvalidName(self) -> None:
        class Tabela(Table):
            __tablename__ = ''
            col = Column(Integer)

        with pytest.raises(InvalidName):
            Tabela()

    def test_quando__tablename__recebe_123_lanca_InvalidName(self) -> None:
        class Tabela(Table):
            __tablename__ = 123
            col = Column(Integer)

        with pytest.raises(InvalidName):
            Tabela()

    def test_quando__tablename__recebe_2teste_lanca_InvalidName(self) -> None:
        class Tabela(Table):
            __tablename__ = '2teste'
            col = Column(Integer)

        with pytest.raises(InvalidName):
            Tabela()

    def test_quando_test_recebe_None_lanca_InvalidTestValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidTestValue):
            Tabela(test=None)

    def test_quando_test_recebe_123_lanca_InvalidTestValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidTestValue):
            Tabela(test=123)

    def test_quando_test_recebe_str_vazia_lanca_InvalidTestValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidTestValue):
            Tabela(test='')

    def test_quando_test_recebe_aaa_lanca_InvalidTestValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidTestValue):
            Tabela(test='aaa')

    def test_quando_create_if_not_exists_recebe_None_lanca_InvalidCreateIfNotExistsValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidCreateIfNotExistsValue):
            Tabela(create_if_not_exists=None)

    def test_quando_create_if_not_exists_recebe_123_lanca_InvalidCreateIfNotExistsValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidCreateIfNotExistsValue):
            Tabela(create_if_not_exists=123)

    def test_quando_create_if_not_exists_recebe_str_vazia_lanca_InvalidCreateIfNotExistsValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidCreateIfNotExistsValue):
            Tabela(create_if_not_exists='')

    def test_quando_create_if_not_exists_recebe_aaa_lanca_InvalidCreateIfNotExistsValue(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

        with pytest.raises(InvalidCreateIfNotExistsValue):
            Tabela(create_if_not_exists='aaa')

    def test_quando__constraints__recebe_123_lanca_InvalidConstraintList(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = 123

        with pytest.raises(InvalidConstraintList):
            Tabela()

    def test_quando__constraints__recebe_str_vazia_lanca_InvalidConstraintList(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = ''

        with pytest.raises(InvalidConstraintList):
            Tabela()

    def test_quando__constraints__recebe_aaa_lanca_InvalidConstraintList(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = 'aaa'

        with pytest.raises(InvalidConstraintList):
            Tabela()

    def test_quando__constraints__recebe_NamedConstraint_e_None_lanca_InvalidConstraintList(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'col'),
                None
            ]

        with pytest.raises(InvalidConstraintList):
            Tabela()

    def test_quando__constraints__recebe_NamedConstraint_e_123_lanca_InvalidConstraintList(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'col'),
                123
            ]

        with pytest.raises(InvalidConstraintList):
            Tabela()

    def test_quando__constraints__recebe_NamedConstraint_e_str_vazia_lanca_InvalidConstraintList(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'col'),
                ''
            ]

        with pytest.raises(InvalidConstraintList):
            Tabela()

    def test_quando__constraints__recebe_NamedConstraint_e_aaa_lanca_InvalidConstraintList(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'col'),
                'aaa'
            ]

        with pytest.raises(InvalidConstraintList):
            Tabela()

    def test_quando__constraints__recebe_2_PrimaryKeyConstraint_lanca_MultiplePrimaryKeyConstraints(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'col'),
                PrimaryKeyConstraint('pk_tabela', 'col')
            ]

        with pytest.raises(MultiplePrimaryKeyConstraints):
            Tabela()

    def test_quando_NamedConstraint_recebe_column_inexistente_lanca_InvalidNamedConstraint(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'inexistente_col')
            ]

        with pytest.raises(InvalidNamedConstraint):
            Tabela()

    def test_quando_MultiColumnNamedConstraint_recebe_column_inexistente_lanca_InvalidNamedConstraint(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', ['inexistente_col', 'col'])
            ]

        with pytest.raises(InvalidNamedConstraint):
            Tabela()

    def test_quando_recebe_ForeignKeyConstraint_com_2_colunas_define_a_constraint_nas_duas_colunas(self) -> None:
        class Tabela(Table):
            col_1 = Column(Integer)
            col_2 = Column(Integer)

            __constraints__ = [
                ForeignKeyConstraint('fk_tabela', ['col_1', 'col_2'], 'tabela', ['id_1', 'id_2'])
            ]

        entry = Tabela(test=True)

        assert entry.col_1.foreign_key is not None
        assert entry.col_2.foreign_key is not None
        assert isinstance(entry.col_1.foreign_key, ForeignKeyConstraint)
        assert isinstance(entry.col_2.foreign_key, ForeignKeyConstraint)

    @pytest.fixture
    def table_1(self) -> Table:
        class Tabela1(Table):
            __tablename__ = 't_setor'

            id = Column(Integer, primary_key=True)
            nome = Column(String(30))

        return Tabela1()

    @pytest.fixture
    def table_2(self) -> Table:
        class Tabela2(Table):
            __tablename__ = 't_funcionario'

            id = Column(Integer, primary_key=True)
            nome = Column(String(50))
            salario = Column(Float(7, 2), default=1212.78)

        return Tabela2()

    def test_quando_duas_tabelas_sao_geradas_a_lista_de_tabelas_contem_elas(self, table_1, table_2) -> None:
        entry = Table.all_tables

        assert table_1 in entry
        assert table_2 in entry

    def test_quando_duas_tabelas_sao_geradas_e_acessamos_a_property_create_query_all_tables(self) -> None:
        result = Table.create_query_all_tables
        expected = 'CREATE TABLE T_SETOR (\n\tid INTEGER NOT NULL,\n\tnome VARCHAR(30) NOT NULL,\n\n\tPRIMARY KEY (id)\n);\n\nCREATE TABLE T_FUNCIONARIO (\n\tid INTEGER NOT NULL,\n\tnome VARCHAR(50) NOT NULL,\n\tsalario FLOAT(7, 2) NOT NULL DEFAULT 1212.78,\n\n\tPRIMARY KEY (id)\n);'

        assert result == expected

    def test_quando_duas_tabelas_sao_geradas_e_salvamos_as_queries_em_arquivo_e_lemos_o_arquivo_retorna_queries(self, tmp_path) -> None:
        tempfile = tmp_path / "mydir/myfile"
        tempfile.parent.mkdir()
        tempfile.touch()

        Table.save_all_tables(tempfile)

        assert tempfile.read_text() == 'CREATE TABLE T_SETOR (\n\tid INTEGER NOT NULL,\n\tnome VARCHAR(30) NOT NULL,\n\n\tPRIMARY KEY (id)\n);\n\nCREATE TABLE T_FUNCIONARIO (\n\tid INTEGER NOT NULL,\n\tnome VARCHAR(50) NOT NULL,\n\tsalario FLOAT(7, 2) NOT NULL DEFAULT 1212.78,\n\n\tPRIMARY KEY (id)\n);'
