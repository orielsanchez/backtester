from _typeshed import Incomplete
from pandas import Categorical as Categorical, Index as Index, IntervalIndex as IntervalIndex
from pandas._libs import Timedelta as Timedelta, Timestamp as Timestamp, lib as lib
from pandas._typing import DtypeObj as DtypeObj, IntervalLeftRight as IntervalLeftRight
from pandas.core.arrays.datetimelike import dtype_to_unit as dtype_to_unit
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_bool_dtype as is_bool_dtype, is_integer as is_integer, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna

def cut(x, bins, right: bool = True, labels: Incomplete | None = None, retbins: bool = False, precision: int = 3, include_lowest: bool = False, duplicates: str = 'raise', ordered: bool = True): ...
def qcut(x, q, labels: Incomplete | None = None, retbins: bool = False, precision: int = 3, duplicates: str = 'raise'): ...
