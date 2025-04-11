import numpy as np
from _typeshed import Incomplete
from pandas import DatetimeIndex, Series, TimedeltaIndex
from pandas._libs.tslibs import Timestamp
from pandas._libs.tslibs.offsets import Day as Day, to_offset as to_offset
from pandas._typing import npt
from pandas.core.arrays.datetimelike import DatetimeLikeArrayMixin

__all__ = ['Day', 'get_period_alias', 'infer_freq', 'is_subperiod', 'is_superperiod', 'to_offset']

def get_period_alias(offset_str: str) -> str | None: ...
def infer_freq(index: DatetimeIndex | TimedeltaIndex | Series | DatetimeLikeArrayMixin) -> str | None: ...

class _FrequencyInferer:
    index: Incomplete
    i8values: Incomplete
    is_monotonic: Incomplete
    def __init__(self, index) -> None: ...
    def deltas(self) -> npt.NDArray[np.int64]: ...
    def deltas_asi8(self) -> npt.NDArray[np.int64]: ...
    def is_unique(self) -> bool: ...
    def is_unique_asi8(self) -> bool: ...
    def get_freq(self) -> str | None: ...
    def day_deltas(self) -> list[int]: ...
    def hour_deltas(self) -> list[int]: ...
    def fields(self) -> np.ndarray: ...
    def rep_stamp(self) -> Timestamp: ...
    def month_position_check(self) -> str | None: ...
    def mdiffs(self) -> npt.NDArray[np.int64]: ...
    def ydiffs(self) -> npt.NDArray[np.int64]: ...

class _TimedeltaFrequencyInferer(_FrequencyInferer): ...

def is_subperiod(source, target) -> bool: ...
def is_superperiod(source, target) -> bool: ...
