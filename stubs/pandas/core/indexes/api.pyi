from pandas._libs import NaT as NaT
from pandas._typing import Axis
from pandas.core.indexes.base import Index as Index, _new_Index as _new_Index, ensure_index as ensure_index, ensure_index_from_sequences as ensure_index_from_sequences, get_unanimous_names as get_unanimous_names
from pandas.core.indexes.category import CategoricalIndex as CategoricalIndex
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.interval import IntervalIndex as IntervalIndex
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.indexes.period import PeriodIndex as PeriodIndex
from pandas.core.indexes.range import RangeIndex as RangeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex
from pandas.errors import InvalidIndexError as InvalidIndexError

__all__ = ['Index', 'MultiIndex', 'CategoricalIndex', 'IntervalIndex', 'RangeIndex', 'InvalidIndexError', 'TimedeltaIndex', 'PeriodIndex', 'DatetimeIndex', '_new_Index', 'NaT', 'ensure_index', 'ensure_index_from_sequences', 'get_objs_combined_axis', 'union_indexes', 'get_unanimous_names', 'all_indexes_same', 'default_index', 'safe_sort_index']

def get_objs_combined_axis(objs, intersect: bool = False, axis: Axis = 0, sort: bool = True, copy: bool = False) -> Index: ...
def safe_sort_index(index: Index) -> Index: ...
def union_indexes(indexes, sort: bool | None = True) -> Index: ...
def all_indexes_same(indexes) -> bool: ...
def default_index(n: int) -> RangeIndex: ...
