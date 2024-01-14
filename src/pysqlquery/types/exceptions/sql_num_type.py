'''
Defines the base exception class for numeric SQL type classes.
'''

from abc import ABCMeta

from .sized_sql_type import SizedSQLTypeException


class SQLNumTypeException(SizedSQLTypeException, metaclass=ABCMeta):
    '''
    Abstract base exception class for numeric SQL type-related exceptions.
    '''
