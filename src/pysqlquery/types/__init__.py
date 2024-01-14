'''
Package for SQL type classes.

There are these classes:

- `Bit` - equivalent to BIT type
- `Boolean` - equivalent to BOOLEAN type
- `Char` - equivalent to CHAR type
- `Date` - equivalent to DATE type
- `DateTime` - equivalent to DATETIME type
- `Decimal` - equivalent to DECIMAL type
- `Double` - equivalent to DOUBLE type
- `Float` - equivalent to FLOAT type
- `Integer` - equivalent to INTEGER or INT type
- `Real` - equivalent to REAL type
- `String` - equivalent to VARCHAR type
- `Time` - equivalent to TIME type
'''

from .string import String
from .float import Float
from .integer import Integer
from .char import Char
from .date import Date
from .datetime import DateTime
from .boolean import Boolean
from .bit import Bit
from .real import Real
from .time import Time
from .double import Double
from .decimal import Decimal
