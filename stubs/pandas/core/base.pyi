import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable, Iterator
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from pandas._config import using_copy_on_write as using_copy_on_write
from pandas._libs import lib as lib
from pandas._typing import AxisInt as AxisInt, DropKeep as DropKeep, DtypeObj as DtypeObj, IndexLabel as IndexLabel, NDFrameT as NDFrameT, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, ScalarLike_co as ScalarLike_co, Self as Self, Shape as Shape, npt as npt
from pandas.compat import PYPY as PYPY
from pandas.core import algorithms as algorithms, nanops as nanops, ops as ops
from pandas.core.accessor import DirNamesMixin as DirNamesMixin
from pandas.core.arraylike import OpsMixin as OpsMixin
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.cast import can_hold_element as can_hold_element
from pandas.core.dtypes.common import is_object_dtype as is_object_dtype, is_scalar as is_scalar
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, remove_na_arraylike as remove_na_arraylike
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Generic, Literal, overload

class PandasObject(DirNamesMixin):
    def __sizeof__(self) -> int: ...

class NoNewAttributesMixin:
    def __setattr__(self, key: str, value) -> None: ...

class SelectionMixin(Generic[NDFrameT]):
    obj: NDFrameT
    exclusions: frozenset[Hashable]
    def ndim(self) -> int: ...
    def __getitem__(self, key): ...
    def aggregate(self, func, *args, **kwargs) -> None: ...
    agg = aggregate

class IndexOpsMixin(OpsMixin):
    __array_priority__: int
    @property
    def dtype(self) -> DtypeObj: ...
    def transpose(self, *args, **kwargs) -> Self: ...
    T: Incomplete
    @property
    def shape(self) -> Shape: ...
    def __len__(self) -> int: ...
    @property
    def ndim(self) -> Literal[1]: ...
    def item(self): ...
    @property
    def nbytes(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def array(self) -> ExtensionArray: ...
    def to_numpy(self, dtype: npt.DTypeLike | None = None, copy: bool = False, na_value: object = ..., **kwargs) -> np.ndarray: ...
    @property
    def empty(self) -> bool: ...
    def argmax(self, axis: AxisInt | None = None, skipna: bool = True, *args, **kwargs) -> int: ...
    def argmin(self, axis: AxisInt | None = None, skipna: bool = True, *args, **kwargs) -> int: ...
    def tolist(self): ...
    to_list = tolist
    def __iter__(self) -> Iterator: ...
    def hasnans(self) -> bool: ...
    def value_counts(self, normalize: bool = False, sort: bool = True, ascending: bool = False, bins: Incomplete | None = None, dropna: bool = True) -> Series: ...
    def unique(self): ...
    def nunique(self, dropna: bool = True) -> int: ...
    @property
    def is_unique(self) -> bool: ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def factorize(self, sort: bool = False, use_na_sentinel: bool = True) -> tuple[npt.NDArray[np.intp], Index]: ...
    @overload
    def searchsorted(self, value: ScalarLike_co, side: Literal['left', 'right'] = ..., sorter: NumpySorter = ...) -> np.intp: ...
    @overload
    def searchsorted(self, value: npt.ArrayLike | ExtensionArray, side: Literal['left', 'right'] = ..., sorter: NumpySorter = ...) -> npt.NDArray[np.intp]: ...
    def drop_duplicates(self, *, keep: DropKeep = 'first'): ...
