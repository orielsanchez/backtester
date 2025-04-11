import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable, Iterator
from pandas._config import using_copy_on_write as using_copy_on_write, warn_copy_on_write as warn_copy_on_write
from pandas._libs import lib as lib
from pandas._libs.tslibs import OutOfBoundsDatetime as OutOfBoundsDatetime
from pandas._typing import ArrayLike as ArrayLike, Axis as Axis, NDFrameT as NDFrameT, npt as npt
from pandas.core import algorithms as algorithms
from pandas.core.arrays import Categorical as Categorical, ExtensionArray as ExtensionArray
from pandas.core.dtypes.common import is_list_like as is_list_like, is_scalar as is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby import ops as ops
from pandas.core.groupby.categorical import recode_for_groupby as recode_for_groupby
from pandas.core.indexes.api import CategoricalIndex as CategoricalIndex, Index as Index, MultiIndex as MultiIndex
from pandas.core.series import Series as Series
from pandas.errors import InvalidIndexError as InvalidIndexError
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level

class Grouper:
    sort: bool
    dropna: bool
    def __new__(cls, *args, **kwargs): ...
    key: Incomplete
    level: Incomplete
    freq: Incomplete
    axis: Incomplete
    binner: Incomplete
    def __init__(self, key: Incomplete | None = None, level: Incomplete | None = None, freq: Incomplete | None = None, axis: Axis | lib.NoDefault = ..., sort: bool = False, dropna: bool = True) -> None: ...
    @property
    def ax(self) -> Index: ...
    @property
    def indexer(self): ...
    @property
    def obj(self): ...
    @property
    def grouper(self): ...
    @property
    def groups(self): ...

class Grouping:
    level: Incomplete
    obj: Incomplete
    in_axis: Incomplete
    grouping_vector: Incomplete
    def __init__(self, index: Index, grouper: Incomplete | None = None, obj: NDFrame | None = None, level: Incomplete | None = None, sort: bool = True, observed: bool = False, in_axis: bool = False, dropna: bool = True, uniques: ArrayLike | None = None) -> None: ...
    def __iter__(self) -> Iterator: ...
    def name(self) -> Hashable: ...
    @property
    def ngroups(self) -> int: ...
    def indices(self) -> dict[Hashable, npt.NDArray[np.intp]]: ...
    @property
    def codes(self) -> npt.NDArray[np.signedinteger]: ...
    @property
    def group_arraylike(self) -> ArrayLike: ...
    @property
    def result_index(self) -> Index: ...
    @property
    def group_index(self) -> Index: ...
    def groups(self) -> dict[Hashable, np.ndarray]: ...

def get_grouper(obj: NDFrameT, key: Incomplete | None = None, axis: Axis = 0, level: Incomplete | None = None, sort: bool = True, observed: bool = False, validate: bool = True, dropna: bool = True) -> tuple[ops.BaseGrouper, frozenset[Hashable], NDFrameT]: ...
