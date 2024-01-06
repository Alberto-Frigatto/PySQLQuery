from ..column import Column


class TableMeta(type):
    def __new__(cls, name, bases, clsdict):
        columns = [val for val in clsdict.values() if isinstance(val, Column)]
        clsdict['_columns'] = columns
        return super().__new__(cls, name, bases, clsdict)
