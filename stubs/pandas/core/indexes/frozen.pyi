from _typeshed import Incomplete
from pandas._typing import Self as Self
from pandas.core.base import PandasObject as PandasObject
from pandas.io.formats.printing import pprint_thing as pprint_thing

class FrozenList(PandasObject, list):
    def union(self, other) -> FrozenList: ...
    def difference(self, other) -> FrozenList: ...
    __add__ = union
    __iadd__ = union
    def __getitem__(self, n): ...
    def __radd__(self, other) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    __req__ = __eq__
    def __mul__(self, other) -> Self: ...
    __imul__ = __mul__
    def __reduce__(self): ...
    def __hash__(self) -> int: ...
    __setitem__: Incomplete
    __setslice__: Incomplete
    __delitem__: Incomplete
    __delslice__: Incomplete
    pop: Incomplete
    append: Incomplete
    extend: Incomplete
    remove: Incomplete
    sort: Incomplete
    insert: Incomplete
