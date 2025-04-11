from pandas._libs import lib as lib
from pandas._libs.tslibs.timedeltas import array_to_timedelta64 as array_to_timedelta64
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, IgnoreRaise as IgnoreRaise
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.dtypes.common import is_object_dtype as is_object_dtype, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype, NumpyEADtype as NumpyEADtype
from pandas.errors import IntCastingNaNError as IntCastingNaNError

def astype_array(values: ArrayLike, dtype: DtypeObj, copy: bool = False) -> ArrayLike: ...
def astype_array_safe(values: ArrayLike, dtype, copy: bool = False, errors: IgnoreRaise = 'raise') -> ArrayLike: ...
def astype_is_view(dtype: DtypeObj, new_dtype: DtypeObj) -> bool: ...
