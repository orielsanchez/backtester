import numpy as np
from datetime import date
from pandas import Series
from pandas._libs.tslibs import Timestamp
from pandas._libs.tslibs.parsing import DateParseError as DateParseError
from pandas._typing import AnyArrayLike, ArrayLike, DateTimeErrorChoices
from pandas.core.indexes.base import Index
from pandas.core.indexes.datetimes import DatetimeIndex
from typing import TypedDict, overload

__all__ = ['DateParseError', 'should_cache', 'to_datetime']

ArrayConvertible = list | tuple | AnyArrayLike
Scalar = float | str
DatetimeScalar = Scalar | date | np.datetime64
DatetimeScalarOrArrayConvertible = DatetimeScalar | ArrayConvertible
DatetimeDictArg = list[Scalar] | tuple[Scalar, ...] | AnyArrayLike

class YearMonthDayDict(TypedDict, total=True):
    year: DatetimeDictArg
    month: DatetimeDictArg
    day: DatetimeDictArg

class FulldatetimeDict(YearMonthDayDict, total=False):
    hour: DatetimeDictArg
    hours: DatetimeDictArg
    minute: DatetimeDictArg
    minutes: DatetimeDictArg
    second: DatetimeDictArg
    seconds: DatetimeDictArg
    ms: DatetimeDictArg
    us: DatetimeDictArg
    ns: DatetimeDictArg

def should_cache(arg: ArrayConvertible, unique_share: float = 0.7, check_count: int | None = None) -> bool: ...
@overload
def to_datetime(arg: DatetimeScalar, errors: DateTimeErrorChoices = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: bool = ..., format: str | None = ..., exact: bool = ..., unit: str | None = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> Timestamp: ...
@overload
def to_datetime(arg: Series | DictConvertible, errors: DateTimeErrorChoices = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: bool = ..., format: str | None = ..., exact: bool = ..., unit: str | None = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> Series: ...
@overload
def to_datetime(arg: list | tuple | Index | ArrayLike, errors: DateTimeErrorChoices = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: bool = ..., format: str | None = ..., exact: bool = ..., unit: str | None = ..., infer_datetime_format: bool = ..., origin=..., cache: bool = ...) -> DatetimeIndex: ...
