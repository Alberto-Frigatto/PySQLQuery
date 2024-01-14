'''
Defines the abstract base class for constructing text SQL type classes.
'''

from abc import ABCMeta

from .sized_sql_type import SizedSQLType


class SQLTextType(SizedSQLType, metaclass=ABCMeta):
    '''
    Abstract class for construct text SQL type classes.

    This class inherits from `SizedSQLType` and provides the basic structures for construct
    concrete classes that represents text SQL types or another
    abstract classes for other kind of text SQL types.

    This class must be inherited by concrete or another abstract one.
    '''
