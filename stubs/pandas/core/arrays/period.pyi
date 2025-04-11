import numpy as np
from _typeshed import Incomplete
from collections.abc import Sequence
from datetime import timedelta
from pandas._libs import lib as lib
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._libs.tslibs import BaseOffset as BaseOffset, NaT as NaT, NaTType as NaTType, Timedelta as Timedelta, add_overflowsafe as add_overflowsafe, astype_overflowsafe as astype_overflowsafe, get_unit_from_dtype as get_unit_from_dtype, iNaT as iNaT, parsing as parsing, period as libperiod, to_offset as to_offset
from pandas._libs.tslibs.dtypes import FreqGroup as FreqGroup, PeriodDtypeBase as PeriodDtypeBase, freq_to_period_freqstr as freq_to_period_freqstr
from pandas._libs.tslibs.fields import isleapyear_arr as isleapyear_arr
from pandas._libs.tslibs.offsets import Tick as Tick, delta_to_tick as delta_to_tick
from pandas._libs.tslibs.period import DIFFERENT_FREQ as DIFFERENT_FREQ, IncompatibleFrequency as IncompatibleFrequency, Period as Period, get_period_field_arr as get_period_field_arr, period_asfreq_arr as period_asfreq_arr
from pandas._typing import AnyArrayLike as AnyArrayLike, Dtype as Dtype, FillnaOptions as FillnaOptions, NpDtype as NpDtype, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, Self as Self, npt as npt
from pandas.core.arrays import DatetimeArray as DatetimeArray, TimedeltaArray as TimedeltaArray, datetimelike as dtl
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.dtypes.common import ensure_object as ensure_object, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries, ABCTimedeltaArray as ABCTimedeltaArray
from pandas.core.dtypes.missing import isna as isna
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Literal, TypeVar, overload

BaseOffsetT = TypeVar('BaseOffsetT', bound=BaseOffset)

class PeriodArray(dtl.DatelikeOps, libperiod.PeriodMixin):
    __array_priority__: int
    def __init__(self, values, dtype: Dtype | None = None, freq: Incomplete | None = None, copy: bool = False) -> None: ...
    def dtype(self) -> PeriodDtype: ...
    @property
    def freq(self) -> BaseOffset: ...
    @property
    def freqstr(self) -> str: ...
    def __array__(self, dtype: NpDtype | None = None, copy: bool | None = None) -> np.ndarray: ...
    def __arrow_array__(self, type: Incomplete | None = None): ...
    year: Incomplete
    month: Incomplete
    day: Incomplete
    hour: Incomplete
    minute: Incomplete
    second: Incomplete
    weekofyear: Incomplete
    week = weekofyear
    day_of_week: Incomplete
    dayofweek = day_of_week
    weekday = dayofweek
    dayofyear: Incomplete
    day_of_year: Incomplete
    quarter: Incomplete
    qyear: Incomplete
    days_in_month: Incomplete
    daysinmonth = days_in_month
    @property
    def is_leap_year(self) -> npt.NDArray[np.bool_]: ...
    def to_timestamp(self, freq: Incomplete | None = None, how: str = 'start') -> DatetimeArray: ...
    def asfreq(self, freq: Incomplete | None = None, how: str = 'E') -> Self: ...
    def astype(self, dtype, copy: bool = True): ...
    def searchsorted(self, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right'] = 'left', sorter: NumpySorter | None = None) -> npt.NDArray[np.intp] | np.intp: ...
    def fillna(self, value: Incomplete | None = None, method: Incomplete | None = None, limit: int | None = None, copy: bool = True) -> Self: ...

def raise_on_incompatible(left, right) -> IncompatibleFrequency: ...
def period_array(data: Sequence[Period | str | None] | AnyArrayLike, freq: str | Tick | BaseOffset | None = None, copy: bool = False) -> PeriodArray: ...
@overload
def validate_dtype_freq(dtype, freq: BaseOffsetT) -> BaseOffsetT: ...
@overload
def validate_dtype_freq(dtype, freq: timedelta | str | None) -> BaseOffset: ...
def dt64arr_to_periodarr(data, freq, tz: Incomplete | None = None) -> tuple[npt.NDArray[np.int64], BaseOffset]: ...
