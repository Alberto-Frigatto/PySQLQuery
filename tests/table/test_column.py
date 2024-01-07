import pytest
from src.pysqlquery.table import Column, Table
from src.pysqlquery.table.exceptions.column import (
    ColumnAlreadyHasNamedForeignKeyConstraint,
    ColumnAlreadyHasNamedUniqueConstraint,
    InvalidAutoIncrement,
    InvalidDefaultValue,
    InvalidForeignKey,
    InvalidNullable,
    InvalidPrimaryKey,
    InvalidSQLType,
    InvalidUnique
)
from src.pysqlquery.types import Integer, Float, String, Char
from src.pysqlquery.constraints import (
    ForeignKey,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint
)


class TestColumn:
    def test_quando_coluna_preco_recebe_data_type_Float_7_2_retorna_preco_FLOAT_7_2_NOT_NULL(self) -> None:
        class Tabela(Table):
            preco = Column(Float(7, 2))

        entry = Tabela(test=True).preco
        result = str(entry)
        expected = 'preco FLOAT(7, 2) NOT NULL'

        assert result == expected

    def test_quando_coluna_preco_recebe_data_type_Float_7_2_e_nullable_True_retorna_preco_FLOAT_7_2(self) -> None:
        class Tabela(Table):
            preco = Column(Float(7, 2), nullable=True)

        entry = Tabela(test=True).preco
        result = str(entry)
        expected = 'preco FLOAT(7, 2)'

        assert result == expected

    def test_quando_coluna_email_recebe_data_type_String_255_e_unique_True_retorna_email_VARCHAR_255_NOT_NULL_UNIQUE(self) -> None:
        class Tabela(Table):
            email = Column(String(255), unique=True)

        entry = Tabela(test=True).email
        result = str(entry)
        expected = 'email VARCHAR(255) NOT NULL UNIQUE'

        assert result == expected

    def test_quando_coluna_saldo_recebe_data_type_Float_7_2_e_default_0_retorna_saldo_Float_7_2_DEFAULT_0(self) -> None:
        class Tabela(Table):
            saldo = Column(Float(7, 2), default=0)

        entry = Tabela(test=True).saldo
        result = str(entry)
        expected = 'saldo FLOAT(7, 2) NOT NULL DEFAULT 0'

        assert result == expected

    def test_quando_coluna_contagem_recebe_data_type_Integer_e_auto_increment_mssql_retorna_contagem_INTEGER_IDENTITY_1_1(self) -> None:
        class Tabela(Table):
            contagem = Column(Integer, auto_increment='mssql')

        entry = Tabela(test=True).contagem
        result = str(entry)
        expected = 'contagem INTEGER IDENTITY(1, 1) NOT NULL'

        assert result == expected

    def test_quando_coluna_contagem_recebe_data_type_Integer_e_auto_increment_mysql_retorna_contagem_INTEGER_AUTO_INCREMENT(self) -> None:
        class Tabela(Table):
            contagem = Column(Integer, auto_increment='mysql')

        entry = Tabela(test=True).contagem
        result = str(entry)
        expected = 'contagem INTEGER AUTO_INCREMENT NOT NULL'

        assert result == expected

    def test_quando_coluna_contagem_recebe_data_type_Integer_e_auto_increment_sqlite_retorna_contagem_INTEGER_AUTO_INCREMENT(self) -> None:
        class Tabela(Table):
            contagem = Column(Integer, auto_increment='sqlite')

        entry = Tabela(test=True).contagem
        result = str(entry)
        expected = 'contagem INTEGER AUTO INCREMENT NOT NULL'

        assert result == expected

    def test_quando_coluna_contagem_recebe_data_type_Integer_e_auto_increment_postgree_retorna_contagem_INTEGER_AUTO_INCREMENT(self) -> None:
        class Tabela(Table):
            contagem = Column(Integer, auto_increment='postgree')

        entry = Tabela(test=True).contagem
        result = str(entry)
        expected = 'contagem INTEGER SERIAL NOT NULL'

        assert result == expected

    def test_quando_coluna_id_recebe_data_type_Integer_e_primary_key_True_retorna_id_INTEGER_NOT_NULL(self) -> None:
        class Tabela(Table):
            id = Column(Integer, primary_key=True)

        entry = Tabela(test=True).id
        result = str(entry)
        expected = 'id INTEGER NOT NULL'

        assert result == expected

    def test_quando_coluna_fk_col_recebe_ForeignKey_e_acessamos_a_property_foreign_keys_retorna_repr(self) -> None:
        class Tabela(Table):
            fk_col = Column(Integer, ForeignKey('other_table', 'id'))

        entry = Tabela(test=True).fk_col.foreign_key
        result = str(entry)
        expected = 'FOREIGN KEY (fk_col) REFERENCES OTHER_TABLE(id)'

        assert result == expected

    def test_quando_tabela_recebe_6_colunas_com_unnamed_constraints_elas_retornam_informacoes(self) -> None:
        class Tabela(Table):
            id = Column(Integer, primary_key=True, auto_increment='mysql')
            nome = Column(String(50))
            sobrenome = Column(String, nullable=True)
            cpf = Column(Char(11), unique=True)
            salario = Column(Float(7, 2), default=1212.78)
            id_setor = Column(Integer, ForeignKey('t_setor', 'id'))

        entry = Tabela(test=True)

        assert str(entry.id) == 'id INTEGER AUTO_INCREMENT NOT NULL'
        assert str(entry.nome) == 'nome VARCHAR(50) NOT NULL'
        assert str(entry.sobrenome) == 'sobrenome VARCHAR'
        assert str(entry.cpf) == 'cpf CHAR(11) NOT NULL UNIQUE'
        assert str(entry.salario) == 'salario FLOAT(7, 2) NOT NULL DEFAULT 1212.78'
        assert str(entry.id_setor) == 'id_setor INTEGER NOT NULL'
        assert str(entry.id.data_type) == 'INTEGER'
        assert str(entry.nome.data_type) == 'VARCHAR(50)'
        assert str(entry.sobrenome.data_type) == 'VARCHAR'
        assert str(entry.cpf.data_type) == 'CHAR(11)'
        assert str(entry.salario.data_type) == 'FLOAT(7, 2)'
        assert str(entry.id_setor.data_type) == 'INTEGER'
        assert isinstance(entry.id.data_type, Integer)
        assert isinstance(entry.nome.data_type, String)
        assert isinstance(entry.sobrenome.data_type, String)
        assert isinstance(entry.cpf.data_type, Char)
        assert isinstance(entry.salario.data_type, Float)
        assert isinstance(entry.id_setor.data_type, Integer)
        assert entry.id.primary_key
        assert not entry.nome.primary_key
        assert not entry.sobrenome.primary_key
        assert not entry.cpf.primary_key
        assert not entry.salario.primary_key
        assert not entry.id_setor.primary_key
        assert entry.id.auto_increment
        assert not entry.nome.auto_increment
        assert not entry.sobrenome.auto_increment
        assert not entry.cpf.auto_increment
        assert not entry.salario.auto_increment
        assert not entry.id_setor.auto_increment
        assert entry.id.name == 'id'
        assert entry.nome.name == 'nome'
        assert entry.sobrenome.name == 'sobrenome'
        assert entry.cpf.name == 'cpf'
        assert entry.salario.name == 'salario'
        assert entry.id_setor.name == 'id_setor'
        assert not entry.id.nullable
        assert not entry.nome.nullable
        assert entry.sobrenome.nullable
        assert not entry.cpf.nullable
        assert not entry.salario.nullable
        assert not entry.id_setor.nullable
        assert entry.id.unique
        assert not entry.nome.unique
        assert not entry.sobrenome.unique
        assert entry.cpf.unique
        assert not entry.salario.unique
        assert not entry.id_setor.unique
        assert entry.id.default is None
        assert entry.nome.default is None
        assert entry.sobrenome.default is None
        assert entry.cpf.default is None
        assert entry.salario.default == 1212.78
        assert entry.id_setor.default is None
        assert entry.id.foreign_key is None
        assert entry.nome.foreign_key is None
        assert entry.sobrenome.foreign_key is None
        assert entry.cpf.foreign_key is None
        assert entry.salario.foreign_key is None
        assert entry.id_setor.foreign_key is not None
        assert isinstance(entry.id_setor.foreign_key, ForeignKey)

    def test_quando_tabela_recebe_6_colunas_com_named_constraints_elas_retornam_informacoes(self) -> None:
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

        entry = Tabela(test=True)

        assert str(entry.id) == 'id INTEGER AUTO_INCREMENT NOT NULL'
        assert str(entry.nome) == 'nome VARCHAR(50) NOT NULL'
        assert str(entry.sobrenome) == 'sobrenome VARCHAR'
        assert str(entry.cpf) == 'cpf CHAR(11) NOT NULL'
        assert str(entry.salario) == 'salario FLOAT(7, 2) NOT NULL DEFAULT 1212.78'
        assert str(entry.id_setor) == 'id_setor INTEGER NOT NULL'
        assert str(entry.id.data_type) == 'INTEGER'
        assert str(entry.nome.data_type) == 'VARCHAR(50)'
        assert str(entry.sobrenome.data_type) == 'VARCHAR'
        assert str(entry.cpf.data_type) == 'CHAR(11)'
        assert str(entry.salario.data_type) == 'FLOAT(7, 2)'
        assert str(entry.id_setor.data_type) == 'INTEGER'
        assert isinstance(entry.id.data_type, Integer)
        assert isinstance(entry.nome.data_type, String)
        assert isinstance(entry.sobrenome.data_type, String)
        assert isinstance(entry.cpf.data_type, Char)
        assert isinstance(entry.salario.data_type, Float)
        assert isinstance(entry.id_setor.data_type, Integer)
        assert entry.id.primary_key
        assert not entry.nome.primary_key
        assert not entry.sobrenome.primary_key
        assert not entry.cpf.primary_key
        assert not entry.salario.primary_key
        assert not entry.id_setor.primary_key
        assert entry.id.auto_increment
        assert not entry.nome.auto_increment
        assert not entry.sobrenome.auto_increment
        assert not entry.cpf.auto_increment
        assert not entry.salario.auto_increment
        assert not entry.id_setor.auto_increment
        assert entry.id.name == 'id'
        assert entry.nome.name == 'nome'
        assert entry.sobrenome.name == 'sobrenome'
        assert entry.cpf.name == 'cpf'
        assert entry.salario.name == 'salario'
        assert entry.id_setor.name == 'id_setor'
        assert not entry.id.nullable
        assert not entry.nome.nullable
        assert entry.sobrenome.nullable
        assert not entry.cpf.nullable
        assert not entry.salario.nullable
        assert not entry.id_setor.nullable
        assert entry.id.unique
        assert not entry.nome.unique
        assert not entry.sobrenome.unique
        assert entry.cpf.unique
        assert not entry.salario.unique
        assert not entry.id_setor.unique
        assert entry.id.default is None
        assert entry.nome.default is None
        assert entry.sobrenome.default is None
        assert entry.cpf.default is None
        assert entry.salario.default == 1212.78
        assert entry.id_setor.default is None
        assert entry.id.foreign_key is None
        assert entry.nome.foreign_key is None
        assert entry.sobrenome.foreign_key is None
        assert entry.cpf.foreign_key is None
        assert entry.salario.foreign_key is None
        assert entry.id_setor.foreign_key is not None
        assert isinstance(entry.id_setor.foreign_key, ForeignKeyConstraint)

    def test_quando_data_type_recebe_None_lanca_InvalidSQLType(self) -> None:
        with pytest.raises(InvalidSQLType):
            Column(None)

    def test_quando_data_type_recebe_123_lanca_InvalidSQLType(self) -> None:
        with pytest.raises(InvalidSQLType):
            Column(123)

    def test_quando_data_type_recebe_aaa_lanca_InvalidSQLType(self) -> None:
        with pytest.raises(InvalidSQLType):
            Column('aaa')

    def test_quando_primary_key_recebe_None_lanca_InvalidPrimaryKey(self) -> None:
        with pytest.raises(InvalidPrimaryKey):
            Column(Integer, primary_key=None)

    def test_quando_primary_key_recebe_123_lanca_InvalidPrimaryKey(self) -> None:
        with pytest.raises(InvalidPrimaryKey):
            Column(Integer, primary_key=123)

    def test_quando_primary_key_recebe_aaa_lanca_InvalidPrimaryKey(self) -> None:
        with pytest.raises(InvalidPrimaryKey):
            Column(Integer, primary_key='aaa')

    def test_quando_auto_increment_recebe_123_lanca_InvalidAutoIncrement(self) -> None:
        with pytest.raises(InvalidAutoIncrement):
            Column(Integer, auto_increment=123)

    def test_quando_auto_increment_recebe_aaa_lanca_InvalidAutoIncrement(self) -> None:
        with pytest.raises(InvalidAutoIncrement):
            Column(Integer, auto_increment='aaa')

    def test_quando_nullable_recebe_None_lanca_InvalidNullable(self) -> None:
        with pytest.raises(InvalidNullable):
            Column(Integer, nullable=None)

    def test_quando_nullable_recebe_123_lanca_InvalidNullable(self) -> None:
        with pytest.raises(InvalidNullable):
            Column(Integer, nullable=123)

    def test_quando_nullable_recebe_aaa_lanca_InvalidNullable(self) -> None:
        with pytest.raises(InvalidNullable):
            Column(Integer, nullable='aaa')

    def test_quando_unique_recebe_None_lanca_InvalidUnique(self) -> None:
        with pytest.raises(InvalidUnique):
            Column(Integer, unique=None)

    def test_quando_unique_recebe_123_lanca_InvalidUnique(self) -> None:
        with pytest.raises(InvalidUnique):
            Column(Integer, unique=123)

    def test_quando_unique_recebe_aaa_lanca_InvalidUnique(self) -> None:
        with pytest.raises(InvalidUnique):
            Column(Integer, unique='aaa')

    def test_quando_data_type_recebe_Integer_2_e_default_recebe_123_int_lanca_InvalidDefaultValue(self) -> None:
        with pytest.raises(InvalidDefaultValue):
            Column(Integer(2), default=123)

    def test_quando_data_type_recebe_Integer_2_e_default_recebe_12_float_lanca_InvalidDefaultValue(self) -> None:
        with pytest.raises(InvalidDefaultValue):
            Column(Integer(2), default=12.)

    def test_quando_data_type_recebe_Integer_2_e_default_recebe_aaa_str_lanca_InvalidDefaultValue(self) -> None:
        with pytest.raises(InvalidDefaultValue):
            Column(Integer(2), default='aaa')

    def test_quando_data_type_recebe_Char_2_e_default_recebe_aaa_str_lanca_InvalidDefaultValue(self) -> None:
        with pytest.raises(InvalidDefaultValue):
            Column(Char(2), default='aaa')

    def test_quando_data_type_recebe_Char_2_e_default_recebe_123_int_lanca_InvalidDefaultValue(self) -> None:
        with pytest.raises(InvalidDefaultValue):
            Column(Char(2), default=123)

    def test_quando_data_type_recebe_Char_2_e_default_recebe_12_float_lanca_InvalidDefaultValue(self) -> None:
        with pytest.raises(InvalidDefaultValue):
            Column(Char(2), default=12.)

    def test_quando_foreign_key_recebe_123_lanca_InvalidForeignKey(self) -> None:
        with pytest.raises(InvalidForeignKey):
            Column(Integer, 123)

    def test_quando_foreign_key_recebe_aaa_lanca_InvalidForeignKey(self) -> None:
        with pytest.raises(InvalidForeignKey):
            Column(Integer, 'aaa')

    def test_quando_tabela_recebe_2_ForeignKeyConstraint_para_mesma_coluna_lanca_ColumnAlreadyHasNamedForeignKeyConstraint(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                ForeignKeyConstraint('fk_const_1', 'col', 'tabela', 'id'),
                ForeignKeyConstraint('fk_const_2', 'col', 'tabela', 'id')
            ]

        with pytest.raises(ColumnAlreadyHasNamedForeignKeyConstraint):
            Tabela(test=True)

    def test_quando_tabela_recebe_2_UniqueConstraint_para_mesma_coluna_lanca_ColumnAlreadyHasNamedUniqueConstraint(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                UniqueConstraint('un_const_1', 'col'),
                UniqueConstraint('un_const_2', 'col')
            ]

        with pytest.raises(ColumnAlreadyHasNamedUniqueConstraint):
            Tabela(test=True)

    def test_quando_coluna_recebe_uma_PrimaryKeyConstraint_na_tabela_e_acessamos_is_primary_key_named_retorna_True(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                PrimaryKeyConstraint('pk_tabela', 'col')
            ]

        entry = Tabela(test=True).col
        result = entry.is_primary_key_named()
        expected = True

        assert result == expected

    def test_quando_coluna_recebe_primary_key_True_e_acessamos_is_primary_key_named_retorna_False(self) -> None:
        class Tabela(Table):
            col = Column(Integer, primary_key=True)

        entry = Tabela(test=True).col
        result = entry.is_primary_key_named()
        expected = False

        assert result == expected

    def test_quando_coluna_recebe_uma_ForeignKeyConstraint_na_tabela_e_acessamos_is_foreign_key_named_retorna_True(self) -> None:
        class Tabela(Table):
            col = Column(Integer)

            __constraints__ = [
                ForeignKeyConstraint('fk_tabela_outra_tabela', 'col', 'outra_tabela', 'id')
            ]

        entry = Tabela(test=True).col
        result = entry.is_foreign_key_named()
        expected = True

        assert result == expected

    def test_quando_coluna_recebe_ForeignKey_e_acessamos_is_foreign_key_named_retorna_False(self) -> None:
        class Tabela(Table):
            col = Column(Integer, ForeignKey('outra_tabela', 'id'))

        entry = Tabela(test=True).col
        result = entry.is_foreign_key_named()
        expected = False

        assert result == expected
