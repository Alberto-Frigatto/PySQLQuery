'''
Defines the Table meta class for constructing SQL tables.
'''

from ..column import Column


class TableMeta(type):
    '''
    This class is used as meta class for SQL table classes.
    '''

    def __new__(mcs, name: str, bases: tuple, clsdict: dict):
        columns = [val for val in clsdict.values() if isinstance(val, Column)]
        clsdict['_columns'] = columns
        return super().__new__(mcs, name, bases, clsdict)
