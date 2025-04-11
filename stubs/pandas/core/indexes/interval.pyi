import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable
from pandas._libs import lib as lib
from pandas._libs.interval import Interval as Interval, IntervalMixin as IntervalMixin, IntervalTree as IntervalTree
from pandas._libs.tslibs import BaseOffset as BaseOffset, Period as Period, Timedelta as Timedelta, Timestamp as Timestamp, to_offset as to_offset
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, IntervalClosedType as IntervalClosedType, Self as Self, npt as npt
from pandas.core.algorithms import unique as unique
from pandas.core.arrays.datetimelike import validate_periods as validate_periods
from pandas.core.arrays.interval import IntervalArray as IntervalArray
from pandas.core.dtypes.cast import find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar, maybe_box_datetimelike as maybe_box_datetimelike, maybe_downcast_numeric as maybe_downcast_numeric, maybe_upcast_numeric_to_64bit as maybe_upcast_numeric_to_64bit
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_number as is_number, is_object_dtype as is_object_dtype, is_scalar as is_scalar, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, IntervalDtype as IntervalDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype
from pandas.core.indexers import is_valid_positional_slice as is_valid_positional_slice
from pandas.core.indexes.base import Index as Index, ensure_index as ensure_index, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, date_range as date_range
from pandas.core.indexes.extension import ExtensionIndex as ExtensionIndex, inherit_names as inherit_names
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex, timedelta_range as timedelta_range
from pandas.errors import InvalidIndexError as InvalidIndexError
from pandas.util._decorators import Appender as Appender, cache_readonly as cache_readonly
from pandas.util._exceptions import rewrite_exception as rewrite_exception
from typing import Any

class IntervalIndex(ExtensionIndex):
    closed: IntervalClosedType
    is_non_overlapping_monotonic: bool
    closed_left: bool
    closed_right: bool
    open_left: bool
    open_right: bool
    def __new__(cls, data, closed: IntervalClosedType | None = None, dtype: Dtype | None = None, copy: bool = False, name: Hashable | None = None, verify_integrity: bool = True) -> Self: ...
    @classmethod
    def from_breaks(cls, breaks, closed: IntervalClosedType | None = 'right', name: Hashable | None = None, copy: bool = False, dtype: Dtype | None = None) -> IntervalIndex: ...
    @classmethod
    def from_arrays(cls, left, right, closed: IntervalClosedType = 'right', name: Hashable | None = None, copy: bool = False, dtype: Dtype | None = None) -> IntervalIndex: ...
    @classmethod
    def from_tuples(cls, data, closed: IntervalClosedType = 'right', name: Hashable | None = None, copy: bool = False, dtype: Dtype | None = None) -> IntervalIndex: ...
    def __contains__(self, key: Any) -> bool: ...
    def __reduce__(self): ...
    @property
    def inferred_type(self) -> str: ...
    def memory_usage(self, deep: bool = False) -> int: ...
    def is_monotonic_decreasing(self) -> bool: ...
    def is_unique(self) -> bool: ...
    @property
    def is_overlapping(self) -> bool: ...
    def get_loc(self, key) -> int | slice | np.ndarray: ...
    def get_indexer_non_unique(self, target: Index) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]: ...
    def left(self) -> Index: ...
    def right(self) -> Index: ...
    def mid(self) -> Index: ...
    @property
    def length(self) -> Index: ...

def interval_range(start: Incomplete | None = None, end: Incomplete | None = None, periods: Incomplete | None = None, freq: Incomplete | None = None, name: Hashable | None = None, closed: IntervalClosedType = 'right') -> IntervalIndex: ...
