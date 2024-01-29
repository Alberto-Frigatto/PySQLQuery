<h1 align="center">
    <img src="./docs/img/logo.png" width="200"/>
    <br/>
    <p style="font-size: 30px">PySQLQuery</p>
</h1>
<p align="center">
    <a href="https://pypi.org/project/pysqlquery/">
        <img src="https://img.shields.io/badge/PyPi-v1.0.0-blue.svg"/>
    </a>
    <a href="https://docs.python.org/3.10/">
        <img src="https://img.shields.io/badge/Python->=%20v3.10-blue.svg"/>
    </a>
    <img src="https://img.shields.io/badge/Coverage-100%25-grren.svg"/>
    <a href="./LICENSE.md">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg"/>
    </a>
    <a href="https://black.readthedocs.io/en/stable/">
        <img src="https://img.shields.io/badge/Code%20style-black-000000.svg"/>
    </a>
</p>

<p align="center">
    <b>PySQLQuery</b> is a simple Python package for generating SQL code. Made to help programmers without much knowledge of SQL, it offers a simple way to generate SQL code using Pythonic techniques.
</p>

# Table of contents

- [Installation](#installation)
- [Docs](#docs)
- [Examples](#examples)
  - [Creating a simple table](#creating-a-simple-table)
  - [Creating a more complex Table](#creating-a-more-complex-table)
  - [Saving all tables that you have been created](#saving-all-tables-that-you-have-been-created)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

# Installation

Using pip:

```bash
pip install pysqlquery
```

# Docs

See our [Docs](./docs/md/docs.md) for comprehensive and detailed documentation on PySQLQuery. In the documentation, you will find in-depth explanations, usage examples, and additional resources to help you maximize your experience with PySQLQuery.

# Examples

## Creating a simple table

```python
from pysqlquery import (
    Table,
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

class TbEmployees(Table):
    id = Column(Integer, primary_key=True, auto_increment='mysql')
    name = Column(String(50))
    email = Column(String(255), unique=True)
    wage = Column(Float(7, 2), default=1250.38)
    id_department = Column(ForeignKey('t_department', 'id'))

tb_emplooyes = TbEmployees()

print(tb_emplooyes)
```

The printed string will be:

```sql
CREATE TABLE TBEMPLOYEES (
    id INTEGER AUTO_INCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    wage FLOAT(7, 2) NOT NULL DEFAULT 1250.38,

    PRIMARY KEY (id),
    FOREIGN KEY (id_department) REFERENCES T_DEPARTMENT(id)
);
```

The provided example demonstrates the process of creating a single table using PySQLQuery, showcasing the simplicity and expressiveness of the package. Let's break down the key elements of the example:

### Importing Required Classes

```python
from pysqlquery import (
    Table,
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
```

The necessary classes are imported from the pysqlquery package. The Column, Table and a data type classes are essential for defining the structure of the SQL table, the constraint ones are optional like ForeignKey.

### Defining the Table

```python
class TbEmployees(Table):
    id = Column(Integer, primary_key=True, auto_increment='mysql')
    name = Column(String(50))
    email = Column(String(255), unique=True)
    wage = Column(Float(7, 2), default=1250.38)
    id_department = Column(ForeignKey('t_department', 'id'))
```

A new table class, TbEmployees, is defined by inheriting from the Table class. Columns such as id, name, and wage are specified using the Column class, each with its respective data type and constraints.

### Creating an Instance of the Table

```python
tb_emplooyes = TbEmployees()
```

An instance of the table, tb_employees, is created.

### Printing the SQL Code

```python
print(tb_emplooyes)
```

The instance of the table is printed, resulting in the corresponding SQL code being generated.

## Creating a more complex Table

```python
from pysqlquery import (
    Table,
    Column,
    Integer,
    String,
    Float
)
from pysqlquery.constraints import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint,
)

class TbEmployees(Table):
    __tablename__ = 'T_EMPLOYEES'
    id = Column(Integer, auto_increment='mysql')
    name = Column(String(50))
    email = Column(String(255))
    wage = Column(Float(7, 2), default=1250.38)
    id_department = Column(Integer)

    __constraints__ = [
        PrimaryKeyConstraint('pk_t_emplooyes', 'id'),
        ForeignKeyConstraint(
            'fk_t_emplooyes_t_department',
            'id_department',
            't_department',
            'id'
        ),
        UniqueConstraint('un_t_emplooyes', 'email')
    ]

tb_emplooyes = TbEmployees(create_if_not_exists=True)

print(tb_emplooyes)
```

The printed string will be:

```sql
CREATE TABLE IF NOT EXISTS T_EMPLOYEES (
    id INTEGER AUTO_INCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    wage FLOAT(7, 2) NOT NULL DEFAULT 1250.38
    id_department INTEGER NOT NULL
);

ALTER TABLE T_EMPLOOYES
    ADD CONSTRAINT pk_t_emplooyes PRIMARY KEY (id);

ALTER TABLE T_EMPLOOYES
    ADD CONSTRAINT fk_t_emplooyes_t_department FOREIGN KEY (id_department) REFERENCES T_DEPARTMENT(id);

ALTER TABLE T_EMPLOOYES
    ADD CONSTRAINT un_t_emplooyes UNIQUE (email);
```

In this extended example, a more complex table is created using PySQLQuery. Let's delve into the key elements specific to this example, without repeating the details covered in the previous one:

### Importing Required Classes and Constraints

```python
from pysqlquery import (
    Table,
    Column,
    Integer,
    String,
    Float
)
from pysqlquery.constraints import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint,
)
```

In addition to the basic classes, this example introduces named constraint classes from the pysqlquery.constraints module, including PrimaryKeyConstraint, ForeignKeyConstraint, and UniqueConstraint.

### Defining the Table

```python
class TbEmployees(Table):
    __tablename__ = 'T_EMPLOYEES'
    id = Column(Integer, auto_increment='mysql')
    name = Column(String(50))
    email = Column(String(255))
    wage = Column(Float(7, 2), default=1250.38)
    id_department = Column(Integer)

    __constraints__ = [
        PrimaryKeyConstraint('pk_t_emplooyes', 'id'),
        ForeignKeyConstraint(
            'fk_t_emplooyes_t_department',
            'id_department',
            't_department',
            'id'
        ),
        UniqueConstraint('un_t_emplooyes', 'email')
    ]
```

This more complex table includes additional specifications such as a table name (```__tablename__```) and named constraint list (```__constraints__```).

## Saving all tables that you have been created

The ```Table``` class provides the ```save_all_tables``` method that will save all tables that you have been created in a file.

```python
Table.save_all_tables('./my_tables.sql')
```

# Contributing

You may contribute in several ways like creating new features, fixing bugs, improving documentation and examples or translating any document here to your language. Find more information in [CONTRIBUTING.md](./docs/md/CONTRIBUTING.md).

# Credits

PySQLQuery is heavily inspired in [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) (for table class structure) and [ArrayMixer](https://github.com/teles/array-mixer/tree/master) (for README).

# License

[MIT](./LICENSE.md) - Alberto Frigatto, 2023
