'''
Package for SQL type classes.

There are these classes:

- `Char` - equivalent to CHAR type
- `Date` - equivalent to DATE type
- `DateTime` - equivalent to DATETIME type
- `Float` - equivalent to FLOAT type
- `Integer` - equivalent to INTEGER or INT type
- `String` - equivalent to VARCHAR type
'''

from .string import String
from .float import Float
from .integer import Integer
from .char import Char
from .date import Date
from .datetime import DateTime
