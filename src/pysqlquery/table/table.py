'''
Defines the Table class for constructing SQL tables.
'''

import re

from ..constraints import ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint
from ..constraints.base.named_constraint import NamedConstraint
from . import Column
from .base import TableMeta
from .exceptions.table import (
    InvalidConstraintList,
    InvalidCreateIfNotExistsValue,
    InvalidName,
    InvalidNamedConstraint,
    InvalidTestValue,
    MultiplePrimaryKeyConstraints,
)


class Table(metaclass=TableMeta):
    '''
    Represents a SQL table.

    This class must be used as superclass for a table class, and subclass must contains
    1 or more Column class for SQL columns as class attributes.
    '''

    __tablename__: str | None = None
    __constraints__: list[NamedConstraint] = None

    _tables: list['Table'] = []

    def __init__(self, *, create_if_not_exists: bool = False, test: bool = False) -> None:
        '''
        Parameters
        ----------
        create_if_not_exists : bool
            If this table must receive the IF NOT EXISTS clause.
        test : bool
            If this table must added to the table global list (True for no).

        Returns
        -------
        None

        Examples
        --------
        Constructing a table class:

        >>> class MyTable(Table):
        >>> ... id = Column(Integer, primary_key=True, auto_increment='mysql')
        >>> ... name = Column(String(50))
        >>> ...
        >>> my_table = MyTable()
        >>> print(my_table)
        CREATE TABLE MYTABLE (
            id INTEGER AUTO_INCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL,

            PRIMARY KEY (id)
        );

        Defining a custom name:

        >>> class MyTable(Table):
        >>> ... __tablename__ = 'tb_customer'
        >>> ... id = Column(Integer, primary_key=True, auto_increment='mysql')
        >>> ... name = Column(String(50))
        >>> ...
        >>> my_table = MyTable()
        >>> print(my_table)
        CREATE TABLE TB_CUSTOMER (
            id INTEGER AUTO_INCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL,

            PRIMARY KEY (id)
        );

        Defining named constraints:

        >>> class MyTable(Table):
        >>> ... __tablename__ = 'tb_customer'
        >>> ... id = Column(Integer, auto_increment='mysql')
        >>> ... name = Column(String(50))
        >>> ... __constraints__ = [PrimaryKeyConstraint('pk_tb_customer', 'id')]
        >>> ...
        >>> my_table = MyTable()
        >>> print(my_table)
        CREATE TABLE TB_CUSTOMER (
            id INTEGER AUTO_INCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL
        );

        ALTER TABLE TB_CUSTOMER
            ADD CONSTRAINT pk_tb_customer PRIMARY KEY (id);

        Adding IF NOT EXISTS clause:

        >>> class MyTable(Table):
        >>> ... __tablename__ = 'tb_customer'
        >>> ... id = Column(Integer, primary_key=True, auto_increment='mysql')
        >>> ... name = Column(String(50))
        >>> ...
        >>> my_table = MyTable(create_if_not_exists=True)
        >>> print(my_table)
        CREATE TABLE IF NOT EXISTS TB_CUSTOMER (
            id INTEGER AUTO_INCREMENT NOT NULL,
            name VARCHAR(50) NOT NULL,

            PRIMARY KEY (id)
        );
        '''

        if self.__tablename__ is not None:
            self._validate_name(self.__tablename__)

        self._name: str = (
            self.__tablename__.strip().upper()
            if self.__tablename__ is not None
            else self.__class__.__name__.upper()
        )

        self._validate_test(test)
        self._test: bool = test

        self._validate_create_if_not_exists(create_if_not_exists)
        self._create_if_not_exists = create_if_not_exists

        if self.__constraints__ is not None:
            self._validate_named_constraints(self.__constraints__)
            self._set_named_constraints_on_columns(self.__constraints__)

        if not self._test:
            self._tables.append(self)

    def _validate_name(self, name: str) -> None:
        if not self._is_name_valid(name):
            raise InvalidName(name)

    def _is_name_valid(self, name: str) -> bool:
        return isinstance(name, str) and re.search(r'^[a-zA-Z][a-zA-Z0-9_]*$', name)

    def _validate_test(self, test: bool) -> None:
        if not self._is_bool(test):
            raise InvalidTestValue(self._name, test)

    def _is_bool(self, test: bool) -> bool:
        return isinstance(test, bool)

    def _validate_create_if_not_exists(self, create_if_not_exists: bool) -> None:
        if not self._is_bool(create_if_not_exists):
            raise InvalidCreateIfNotExistsValue(self._name, create_if_not_exists)

    def _validate_named_constraints(self, constraints: list[NamedConstraint]) -> None:
        if not self._is_constraint_list_valid(constraints):
            raise InvalidConstraintList(self._name)

        if self._are_there_multiple_pk_constraints(constraints):
            raise MultiplePrimaryKeyConstraints(self._name)

        for constraint in constraints:
            if isinstance(constraint.column, str):
                if not self._is_constraint_column_a_valid_table_column(constraint.column):
                    raise InvalidNamedConstraint(self._name, constraint.name)
            else:
                for column in constraint.column:
                    if not self._is_constraint_column_a_valid_table_column(column):
                        raise InvalidNamedConstraint(self._name, constraint.name)

    def _is_constraint_list_valid(self, constraints: list[NamedConstraint]) -> bool:
        if isinstance(constraints, list):
            for constraint in constraints:
                if not isinstance(constraint, NamedConstraint):
                    return False

            return True

        return False

    def _are_there_multiple_pk_constraints(self, constraints: list[NamedConstraint]) -> bool:
        pk_consts = [
            constraint for constraint in constraints if isinstance(constraint, PrimaryKeyConstraint)
        ]

        return len(pk_consts) > 1

    def _is_constraint_column_a_valid_table_column(self, constraint_column: str) -> bool:
        for column in self.columns:
            if constraint_column == column.name:
                break
        else:
            return False

        return True

    def _set_named_constraints_on_columns(self, constraints: list[NamedConstraint]) -> None:
        pk_consts = [
            constraint for constraint in constraints if isinstance(constraint, PrimaryKeyConstraint)
        ]
        fk_consts = [
            constraint for constraint in constraints if isinstance(constraint, ForeignKeyConstraint)
        ]
        un_consts = [
            constraint for constraint in constraints if isinstance(constraint, UniqueConstraint)
        ]

        for pk_const in pk_consts:
            self._set_named_primary_key_on_column(pk_const.column)

        for fk_const in fk_consts:
            self._set_named_foreign_key_on_column(fk_const)

        for un_const in un_consts:
            self._set_named_unique_on_column(un_const.column)

    def _set_named_primary_key_on_column(self, const_column: str | list[str]) -> None:
        for table_column in self._columns:
            if isinstance(const_column, str):
                if table_column.name == const_column:
                    table_column.define_primary_key_from_named_constraint()
            else:
                for const_column_name in const_column:
                    if table_column.name == const_column_name:
                        table_column.define_primary_key_from_named_constraint()

    def _set_named_foreign_key_on_column(self, fk_const: ForeignKeyConstraint) -> None:
        for table_column in self._columns:
            if isinstance(fk_const.column, str):
                if table_column.name == fk_const.column:
                    table_column.define_foreign_key_from_named_constraint(fk_const)
            else:
                for const_column_name in fk_const.column:
                    if table_column.name == const_column_name:
                        table_column.define_foreign_key_from_named_constraint(fk_const)

    def _set_named_unique_on_column(self, const_column: str) -> None:
        for table_column in self._columns:
            if table_column.name == const_column:
                table_column.define_unique_from_named_constraint()

    def __str__(self) -> str:
        '''
        Returns
        -------
        str
            A string representation of the class instance in SQL format.
        '''

        unnamed_pk_consts_str = ''
        unnamed_pk_consts = [
            column.name for column in self.primary_key if not column.is_primary_key_named()
        ]

        if unnamed_pk_consts:
            unnamed_pk_consts_str = f'PRIMARY KEY ({", ".join(unnamed_pk_consts)})'

        unnamed_fk_consts_str = ''
        unnamed_fk_consts = [
            str(column.foreign_key)
            for column in self._columns
            if column.foreign_key
            if not column.is_foreign_key_named()
        ]

        if unnamed_fk_consts:
            unnamed_fk_consts_str = ",\n\t".join(unnamed_fk_consts)

        unnamed_consts = (
            unnamed_pk_consts_str
            + (',\n\t' if unnamed_pk_consts_str and unnamed_fk_consts_str else '')
            + unnamed_fk_consts_str
        )

        columns_str = ',\n\t'.join(str(column) for column in self._columns)

        if unnamed_consts:
            columns_str += ',\n\n\t'

        table_repr = (
            f"CREATE TABLE{' IF NOT EXISTS' if self._create_if_not_exists else ''} "
            f"{self._name} (\n\t{columns_str}{unnamed_consts}\n);"
        )

        if self.__constraints__ is not None:
            for constraint in self.__constraints__:
                table_repr += f'\n\nALTER TABLE {self._name}\n\t{"ADD " + str(constraint)};'

        return table_repr

    @classmethod
    def save_all_tables(cls, path: str, encoding: str = 'UTF-8') -> None:
        with open(path, 'w', encoding=encoding) as file:
            file.write(cls.create_query_all_tables)

    @property
    def tablename(self) -> str:
        return self._name

    @property
    def columns(self) -> list[Column]:
        return self._columns

    @property
    def primary_key(self) -> list[Column]:
        pk_columns = [column for column in self._columns if column.primary_key]

        return pk_columns

    @property
    def named_constraints(self) -> list[NamedConstraint] | None:
        return self.__constraints__

    @property
    def test(self) -> bool:
        return self._test

    @classmethod
    @property
    def all_tables(cls) -> list['Table']:
        return cls._tables

    @classmethod
    @property
    def create_query_all_tables(cls) -> str | None:
        return '\n\n'.join([str(table) for table in cls._tables]) if cls._tables else None
