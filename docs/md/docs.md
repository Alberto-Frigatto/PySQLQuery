# Docs

Explore the comprehensive documentation offered by **PySQLQuery**, a Python package dedicated to simplifying working with SQL queries.

Whether you are a beginner or an experienced developer, this guide offers **detailed explanations** to make the package easier to understand and use efficiently.

# Topics

- <a href="./sql_types.md">SQL data types</a>
- <a href="./constraints.md">SQL constraints</a>
- <a href="./table.md">SQL Table and column</a>
- [Project Structure](#project-structure)
- Class diagrams
  - <a href="../pdf/constraints.pdf">Constraints</a>
  - <a href="../pdf/table.pdf">Table and column</a>
  - <a href="../pdf/sql_types.pdf">Data types</a>

## Project structure

```sh
└── pysqlquery/
    ├── constraints/
    │   ├── base/
    │   │   ├── constraint.py
    │   │   ├── multi_column_named_constraint.py
    │   │   ├── named_constraint.py
    │   │   ├── single_column_named_constraint.py
    │   │   └── unnamed_constraint.py
    │   ├── exceptions/
    │   │   ├── constraint.py
    │   │   ├── multi_column_named_constraint.py
    │   │   ├── named_constraint.py
    │   │   ├── named_foreign_key.py
    │   │   ├── unnamed_constraint.py
    │   │   └── unnamed_foreign_key.py
    │   ├── named/
    │   │   ├── foreign_key.py
    │   │   ├── primary_key.py
    │   │   └── unique.py
    │   └── unnamed/
    │       └── foreign_key.py
    ├── table/
    │   ├── base/
    │   │   └── table_meta.py
    │   ├── column.py
    │   ├── exceptions/
    │   │   ├── column.py
    │   │   └── table.py
    │   └── table.py
    └── types/
        ├── base/
        │   ├── sql_date_type.py
        │   ├── sql_decimal_type.py
        │   ├── sql_int_type.py
        │   ├── sql_num_type.py
        │   ├── sql_text_type.py
        │   └── sql_type.py
        ├── bit.py
        ├── boolean.py
        ├── char.py
        ├── date.py
        ├── datetime.py
        ├── decimal.py
        ├── double.py
        ├── exceptions/
        │   ├── sql_date_type.py
        │   ├── sql_decimal_type.py
        │   ├── sql_num_type.py
        │   ├── sql_text_type.py
        │   └── sql_type.py
        ├── float.py
        ├── integer.py
        ├── real.py
        ├── string.py
        └── time.py

```
