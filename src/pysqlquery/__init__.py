'''
`PySQLQuery`
============

Simple Python package for generating SQL code.

Made to help programmers without much knowledge of SQL,
it offers a simple way to generate SQL code using Pythonic techniques.

Github link https://github.com/Alberto-Frigatto/PySQLQuery
PyPi link https://pypi.org/project/pysqlquery/
'''

from .constraints import ForeignKey
from .table import Column, Table
from .types import Char, Date, DateTime, Float, Integer, String
