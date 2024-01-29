'''
Defines the abstract base class for constructing integer SQL type classes.
'''

from abc import ABCMeta

from .sql_num_type import SQLNumType


class SQLIntType(SQLNumType, metaclass=ABCMeta):
    '''
    Abstract class for construct integer SQL type classes.

    This class inherits from `SQLNumType` and provides the basic structures for construct
    concrete classes that represents integer SQL types or another
    abstract classes for other kind of integer SQL types.

    This class must be inherited by concrete or another abstract one.
    '''
