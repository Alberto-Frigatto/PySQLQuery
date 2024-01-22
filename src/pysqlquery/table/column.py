'''
Defines the Column class for constructing SQL table columns.
'''

from typing import Any, Literal

from ..constraints import ForeignKey, ForeignKeyConstraint
from ..types.base.sql_num_type import SQLNumType
from ..types.base.sql_type import SQLType
from .exceptions.column import (
    ColumnAlreadyHasNamedForeignKeyConstraint,
    ColumnAlreadyHasNamedUniqueConstraint,
    InvalidAutoIncrement,
    InvalidDefaultValue,
    InvalidForeignKey,
    InvalidNullable,
    InvalidPrimaryKey,
    InvalidSQLType,
    InvalidUnique,
)


class Column:
    '''
    Represents a SQL table column.

    This class must be used in a SQL table class.

    If named constraints are passed in a table, they can modifying table's columns.
    '''

    def __init__(
        self,
        data_type: SQLType,
        foreign_key: ForeignKey | None = None,
        *,
        primary_key: bool = False,
        auto_increment: Literal['mssql', 'mysql', 'sqlite', 'postgree'] | None = None,
        nullable: bool = False,
        unique: bool = False,
        default: Any = None,
    ) -> None:
        '''
        Parameters
        ----------
        data_type : SQLType
            The column's data type (can be a class or a instance).
        foreign_key : ForeignKey | None
            The column's unnamed FOREIGN KEY constraint.
        primary_key : bool
            If the column is primary key.
        auto_increment : str | None
            The kind of auto increment that column can receive.
        nullable : bool
            If the column is nullable.
        unique : bool
            If the column is unique.
        default : Any
            The column's default value (must satisfying the column's data type).

        Returns
        -------
        None

        Examples
        --------
        A simple column:

        >>> class MyTable(Table):
        >>> ... col = Column(Integer)
        >>> ...
        >>> my_table = MyTable()
        >>> print(my_table.col)
        col INTEGER NOT NULL

        Columns with some modifiers:

        >>> class TbProducts(Table):
        >>> ... id = Column(Integer(6), primary_key=True, auto_incremente='mysql')
        >>> ... name = Column(String(50), unique=True)
        >>> ... price = Column(Float(7, 2), default=1)

        When `NamedConstraint` is passed for table, it can modifying this column.

        >>> class MyTable(Table):
        >>> ... un_col = Column(Char(10))
        >>> ... __constraints__ = [UniqueConstraint('un_my_table_un_col', 'un_col')]
        >>> ...
        >>> my_table = MyTable()
        >>> my_table.un_col.unique
        True
        '''

        self._validate_data_type(data_type)
        self._data_type: SQLType = self._handle_data_type(data_type)

        self._validate_unnamed_fk(foreign_key)
        self._unnamed_foreign_key: ForeignKey | None = foreign_key

        self._validate_primary_key(primary_key)
        self._unnamed_primary_key: bool = primary_key

        self._allowed_kinds_of_auto_increment: dict[str, str] = {
            'mssql': 'IDENTITY(1, 1)',
            'mysql': 'AUTO_INCREMENT',
            'sqlite': 'AUTO INCREMENT',
            'postgree': 'SERIAL',
        }

        self._validate_auto_increment(auto_increment)
        self._auto_increment: str = (
            self._handle_auto_increment(auto_increment) if auto_increment is not None else None
        )

        self._validate_nullable(nullable)
        self._nullable: bool = nullable

        self._validate_unique(unique)
        self._unnamed_unique: bool = unique

        self._validate_default_value(default)
        self._default: Any = default

        self._unnamed_constraints_repr: tuple[str | None] = None
        self._name: str = None

        self._named_primary_key: bool = False
        self._named_foreign_key: ForeignKeyConstraint | None = None
        self._named_unique: bool = False

        self._define_unnamed_constraints_if_wrong()
        self._set_constraints_repr()

    def _validate_data_type(self, data_type: SQLType) -> None:
        if not self._is_data_type_valid(data_type):
            raise InvalidSQLType(data_type)

    def _is_data_type_valid(self, data_type: SQLType) -> bool:
        return (isinstance(data_type, type) and issubclass(data_type, SQLType)) or isinstance(
            data_type, SQLType
        )

    def _validate_unnamed_fk(self, foreign_key: ForeignKey | None) -> None:
        if not self._is_foreign_key_valid(foreign_key):
            raise InvalidForeignKey(foreign_key)

    def _is_foreign_key_valid(self, foreign_key: ForeignKey | None) -> bool:
        return foreign_key is None or isinstance(foreign_key, ForeignKey)

    def _validate_primary_key(self, primary_key: bool) -> None:
        if not self._is_bool(primary_key):
            raise InvalidPrimaryKey(primary_key)

    def _is_bool(self, value: Any) -> bool:
        return isinstance(value, bool)

    def _validate_auto_increment(self, auto_increment: str | None) -> None:
        if not self._is_auto_increment_valid(auto_increment):
            raise InvalidAutoIncrement(auto_increment)

    def _is_auto_increment_valid(self, auto_increment: str | None):
        return (
            auto_increment is None
            or isinstance(auto_increment, str)
            and auto_increment.lower() in self._allowed_kinds_of_auto_increment
        )

    def _validate_nullable(self, nullable: bool) -> None:
        if not self._is_bool(nullable):
            raise InvalidNullable(nullable)

    def _validate_unique(self, unique: bool) -> None:
        if not self._is_bool(unique):
            raise InvalidUnique(unique)

    def _validate_default_value(self, default_value: Any) -> None:
        if not self._is_default_value_valid(default_value):
            raise InvalidDefaultValue(self.data_type, default_value)

    def _is_default_value_valid(self, default_value: Any) -> bool:
        return default_value is None or self._data_type.validate_value(default_value)

    def _handle_data_type(self, data_type: SQLType) -> SQLType:
        return data_type() if isinstance(data_type, type) else data_type

    def _handle_auto_increment(self, auto_increment: str) -> str:
        return self._allowed_kinds_of_auto_increment[auto_increment]

    def __set_name__(self, owner, name: str) -> None:
        self._name = name.strip().lower()

        if self._unnamed_foreign_key is not None:
            self._unnamed_foreign_key.add_column_name(name)

    def __str__(self) -> str:
        '''
        Returns
        -------
        str
            A string representation of the class instance in SQL format.
        '''

        constraints_str = " ".join(
            constraint for constraint in self._unnamed_constraints_repr if constraint
        )

        return f"{self._name} {self._data_type}{' ' + constraints_str if constraints_str else ''}"

    def _define_unnamed_constraints_if_wrong(self) -> None:
        self._set_nullable_if_wrong()
        self._set_unique_if_wrong()

    def _set_nullable_if_wrong(self) -> None:
        self._nullable = not self._unnamed_primary_key and self._nullable

    def _set_unique_if_wrong(self) -> None:
        self._unnamed_unique = self._unnamed_primary_key or self._unnamed_unique

    def _set_constraints_repr(self) -> None:
        ai_constraint = self._get_auto_increment_constraint_repr()
        null_constraint = self._get_nullable_constraint_repr()
        un_constraint = self._get_unique_constraint_repr()
        default_value = self._get_default_value_constraint_repr()

        self._unnamed_constraints_repr = (
            ai_constraint,
            null_constraint,
            un_constraint,
            default_value,
        )

    def _get_auto_increment_constraint_repr(self) -> str | None:
        return (
            self._auto_increment
            if self._auto_increment and isinstance(self._data_type, SQLNumType)
            else None
        )

    def _get_nullable_constraint_repr(self) -> str | None:
        return None if not self._unnamed_primary_key and self._nullable else 'NOT NULL'

    def _get_unique_constraint_repr(self) -> str | None:
        return 'UNIQUE' if not self._unnamed_primary_key and self._unnamed_unique else None

    def _get_default_value_constraint_repr(self) -> str | None:
        return f'DEFAULT {self._default!r}' if self._default is not None else None

    def define_primary_key_from_named_constraint(self) -> None:
        '''
        Define this column as primary key from a table's named constraint.

        `This method shouldn't be used`. It's used by `pysqlquery` automatically when you adds
        this constraint in a Table.
        '''

        self._nullable = False
        self._named_primary_key = True
        self._set_constraints_repr()
        self._unnamed_unique = True

    def define_foreign_key_from_named_constraint(self, fk_const: ForeignKeyConstraint) -> None:
        '''
        Define this column as foreign key from a table's named constraint.

        `This method shouldn't be used`. It's used by `pysqlquery` automatically when you adds
        this constraint in a Table.
        '''

        if self._named_foreign_key is not None:
            raise ColumnAlreadyHasNamedForeignKeyConstraint(self._name)

        self._named_foreign_key = fk_const

    def define_unique_from_named_constraint(self) -> None:
        '''
        Define this column as unique from a table's named constraint.

        `This method shouldn't be used`. It's used by `pysqlquery` automatically when you adds
        this constraint in a Table.
        '''

        if self._named_unique:
            raise ColumnAlreadyHasNamedUniqueConstraint(self._name)

        self._named_unique = True

    def is_primary_key_named(self) -> bool:
        '''
        Return if this column is primary key from unnamed or named constraint if this column
        is primary key.

        `This method shouldn't be used`. It's used by `pysqlquery` automatically when you adds
        this constraint in a Table.
        '''

        return bool(self._named_primary_key)

    def is_foreign_key_named(self) -> bool:
        '''
        Return if this column is foreign key from unnamed or named constraint if this column
        is foreign key.

        `This method shouldn't be used`. It's used by `pysqlquery` automatically when you adds
        this constraint in a Table.
        '''

        return bool(self._named_foreign_key)

    @property
    def name(self) -> str:
        return self._name

    @property
    def data_type(self) -> SQLType:
        return self._data_type

    @property
    def foreign_key(self) -> ForeignKey | ForeignKeyConstraint | None:
        return self._unnamed_foreign_key or self._named_foreign_key

    @property
    def primary_key(self) -> bool:
        return self._unnamed_primary_key or self._named_primary_key

    @property
    def auto_increment(self) -> bool:
        return bool(self._auto_increment)

    @property
    def nullable(self) -> bool:
        return self._nullable

    @property
    def unique(self) -> bool:
        return self._unnamed_unique or self._named_unique

    @property
    def default(self) -> Any:
        return self._default
