from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._libs.tslibs import Resolution as Resolution, Timedelta as Timedelta, to_offset as to_offset
from pandas._libs.tslibs.timedeltas import disallow_ambiguous_unit as disallow_ambiguous_unit
from pandas._typing import DtypeObj as DtypeObj
from pandas.core.arrays.timedeltas import TimedeltaArray as TimedeltaArray
from pandas.core.dtypes.common import is_scalar as is_scalar, pandas_dtype as pandas_dtype
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.indexes.base import Index as Index, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin as DatetimeTimedeltaMixin
from pandas.core.indexes.extension import inherit_names as inherit_names
from pandas.util._exceptions import find_stack_level as find_stack_level

class TimedeltaIndex(DatetimeTimedeltaMixin):
    def __new__(cls, data: Incomplete | None = None, unit=..., freq=..., closed=..., dtype: Incomplete | None = None, copy: bool = False, name: Incomplete | None = None): ...
    def get_loc(self, key): ...
    @property
    def inferred_type(self) -> str: ...

def timedelta_range(start: Incomplete | None = None, end: Incomplete | None = None, periods: int | None = None, freq: Incomplete | None = None, name: Incomplete | None = None, closed: Incomplete | None = None, *, unit: str | None = None) -> TimedeltaIndex: ...
