'''
Package for SQL constraint classes.

There are these classes:

- `ForeignKey` - for unnamed FOREIGN KEY constraint
- `ForeignKeyConstraint` - for named FOREIGN KEY constraint
- `PrimaryKeyConstraint` - for named PRIMARY KEY constraint
- `UniqueConstraint` - for named UNIQUE constraint
'''

from .unnamed import ForeignKey
from .named import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint
)
