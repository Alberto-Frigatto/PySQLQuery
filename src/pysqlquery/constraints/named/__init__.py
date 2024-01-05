'''
Package for named SQL constraint classes.

There are these classes:

- `ForeignKeyConstraint`
- `PrimaryKeyConstraint`
- `UniqueConstraint`
'''

from .foreign_key import ForeignKeyConstraint
from .primary_key import PrimaryKeyConstraint
from .unique import UniqueConstraint
