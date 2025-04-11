from _typeshed import Incomplete
from collections.abc import Hashable
from pandas import DataFrame as DataFrame, Series as Series
from pandas._libs import lib as lib
from pandas._libs.tslibs import BaseOffset as BaseOffset, IncompatibleFrequency as IncompatibleFrequency, NaT as NaT, Period as Period, Timedelta as Timedelta, Timestamp as Timestamp, to_offset as to_offset
from pandas._libs.tslibs.dtypes import freq_to_period_freqstr as freq_to_period_freqstr
from pandas._typing import AnyArrayLike as AnyArrayLike, Axis as Axis, AxisInt as AxisInt, Frequency as Frequency, IndexLabel as IndexLabel, InterpolateOptions as InterpolateOptions, NDFrameT as NDFrameT, T as T, TimeGrouperOrigin as TimeGrouperOrigin, TimedeltaConvertibleTypes as TimedeltaConvertibleTypes, TimestampConvertibleTypes as TimestampConvertibleTypes, npt as npt
from pandas.core.apply import ResamplerWindowApply as ResamplerWindowApply, warn_alias_replacement as warn_alias_replacement
from pandas.core.arrays import ArrowExtensionArray as ArrowExtensionArray
from pandas.core.base import PandasObject as PandasObject, SelectionMixin as SelectionMixin
from pandas.core.dtypes.dtypes import ArrowDtype as ArrowDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby.generic import SeriesGroupBy as SeriesGroupBy
from pandas.core.groupby.groupby import BaseGroupBy as BaseGroupBy, GroupBy as GroupBy, get_groupby as get_groupby
from pandas.core.groupby.grouper import Grouper as Grouper
from pandas.core.groupby.ops import BinGrouper as BinGrouper
from pandas.core.indexes.api import MultiIndex as MultiIndex
from pandas.core.indexes.base import Index as Index
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex, date_range as date_range
from pandas.core.indexes.period import PeriodIndex as PeriodIndex, period_range as period_range
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex, timedelta_range as timedelta_range
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.tseries.frequencies import is_subperiod as is_subperiod, is_superperiod as is_superperiod
from pandas.tseries.offsets import Day as Day, Tick as Tick
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level, rewrite_warning as rewrite_warning
from typing import Callable, Literal

class Resampler(BaseGroupBy, PandasObject):
    binner: DatetimeIndex | TimedeltaIndex | PeriodIndex
    exclusions: frozenset[Hashable]
    keys: Incomplete
    sort: bool
    axis: Incomplete
    kind: Incomplete
    group_keys: Incomplete
    as_index: bool
    include_groups: Incomplete
    def __init__(self, obj: NDFrame, timegrouper: TimeGrouper, axis: Axis = 0, kind: Incomplete | None = None, *, gpr_index: Index, group_keys: bool = False, selection: Incomplete | None = None, include_groups: bool = True) -> None: ...
    def __getattr__(self, attr: str): ...
    def pipe(self, func: Callable[..., T] | tuple[Callable[..., T], str], *args, **kwargs) -> T: ...
    def aggregate(self, func: Incomplete | None = None, *args, **kwargs): ...
    agg = aggregate
    apply = aggregate
    def transform(self, arg, *args, **kwargs): ...
    def ffill(self, limit: int | None = None): ...
    def nearest(self, limit: int | None = None): ...
    def bfill(self, limit: int | None = None): ...
    def fillna(self, method, limit: int | None = None): ...
    def interpolate(self, method: InterpolateOptions = 'linear', *, axis: Axis = 0, limit: int | None = None, inplace: bool = False, limit_direction: Literal['forward', 'backward', 'both'] = 'forward', limit_area: Incomplete | None = None, downcast=..., **kwargs): ...
    def asfreq(self, fill_value: Incomplete | None = None): ...
    def sum(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def prod(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def min(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def max(self, numeric_only: bool = False, min_count: int = 0, *args, **kwargs): ...
    def first(self, numeric_only: bool = False, min_count: int = 0, skipna: bool = True, *args, **kwargs): ...
    def last(self, numeric_only: bool = False, min_count: int = 0, skipna: bool = True, *args, **kwargs): ...
    def median(self, numeric_only: bool = False, *args, **kwargs): ...
    def mean(self, numeric_only: bool = False, *args, **kwargs): ...
    def std(self, ddof: int = 1, numeric_only: bool = False, *args, **kwargs): ...
    def var(self, ddof: int = 1, numeric_only: bool = False, *args, **kwargs): ...
    def sem(self, ddof: int = 1, numeric_only: bool = False, *args, **kwargs): ...
    def ohlc(self, *args, **kwargs): ...
    def nunique(self, *args, **kwargs): ...
    def size(self): ...
    def count(self): ...
    def quantile(self, q: float | list[float] | AnyArrayLike = 0.5, **kwargs): ...

class _GroupByMixin(PandasObject, SelectionMixin):
    binner: Incomplete
    key: Incomplete
    ax: Incomplete
    obj: Incomplete
    include_groups: Incomplete
    def __init__(self, *, parent: Resampler, groupby: GroupBy, key: Incomplete | None = None, selection: IndexLabel | None = None, include_groups: bool = False) -> None: ...

class DatetimeIndexResampler(Resampler):
    ax: DatetimeIndex

class DatetimeIndexResamplerGroupby(_GroupByMixin, DatetimeIndexResampler): ...

class PeriodIndexResampler(DatetimeIndexResampler):
    ax: PeriodIndex

class PeriodIndexResamplerGroupby(_GroupByMixin, PeriodIndexResampler): ...

class TimedeltaIndexResampler(DatetimeIndexResampler):
    ax: TimedeltaIndex

class TimedeltaIndexResamplerGroupby(_GroupByMixin, TimedeltaIndexResampler): ...

def get_resampler(obj: Series | DataFrame, kind: Incomplete | None = None, **kwds) -> Resampler: ...
def get_resampler_for_grouping(groupby: GroupBy, rule, how: Incomplete | None = None, fill_method: Incomplete | None = None, limit: int | None = None, kind: Incomplete | None = None, on: Incomplete | None = None, include_groups: bool = True, **kwargs) -> Resampler: ...

class TimeGrouper(Grouper):
    origin: TimeGrouperOrigin
    closed: Incomplete
    label: Incomplete
    kind: Incomplete
    convention: Incomplete
    how: Incomplete
    fill_method: Incomplete
    limit: Incomplete
    group_keys: Incomplete
    offset: Incomplete
    def __init__(self, obj: Grouper | None = None, freq: Frequency = 'Min', key: str | None = None, closed: Literal['left', 'right'] | None = None, label: Literal['left', 'right'] | None = None, how: str = 'mean', axis: Axis = 0, fill_method: Incomplete | None = None, limit: int | None = None, kind: str | None = None, convention: Literal['start', 'end', 'e', 's'] | None = None, origin: Literal['epoch', 'start', 'start_day', 'end', 'end_day'] | TimestampConvertibleTypes = 'start_day', offset: TimedeltaConvertibleTypes | None = None, group_keys: bool = False, **kwargs) -> None: ...

def asfreq(obj: NDFrameT, freq, method: Incomplete | None = None, how: Incomplete | None = None, normalize: bool = False, fill_value: Incomplete | None = None) -> NDFrameT: ...
def maybe_warn_args_and_kwargs(cls, kernel: str, args, kwargs) -> None: ...
