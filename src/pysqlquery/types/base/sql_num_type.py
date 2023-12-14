'''
Defines the abstract base class for constructing numeric SQL type classes.
'''

from abc import ABCMeta
from .sized_sql_type import SizedSQLType


class SQLNumType(SizedSQLType, metaclass=ABCMeta):
    '''
    Abstract class for construct numeric SQL type classes.

    This class inherits from `SizedSQLType` and provides the basic structures for construct
    another abstract classes for other kind of numeric SQL types.

    This class must be inherited by abstract one.
    '''
    pass
