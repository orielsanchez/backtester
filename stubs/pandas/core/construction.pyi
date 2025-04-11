import numpy as np
from collections.abc import Sequence
from numpy import ma
from pandas import Index as Index, Series as Series
from pandas._config import using_pyarrow_string_dtype as using_pyarrow_string_dtype
from pandas._libs import lib as lib
from pandas._libs.tslibs import Period as Period, get_supported_dtype as get_supported_dtype, is_supported_dtype as is_supported_dtype
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, Dtype as Dtype, DtypeObj as DtypeObj, T as T
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, construct_1d_object_array_from_listlike as construct_1d_object_array_from_listlike, maybe_cast_to_datetime as maybe_cast_to_datetime, maybe_cast_to_integer_array as maybe_cast_to_integer_array, maybe_convert_platform as maybe_convert_platform, maybe_infer_to_datetimelike as maybe_infer_to_datetimelike, maybe_promote as maybe_promote
from pandas.core.dtypes.common import is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import NumpyEADtype as NumpyEADtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCExtensionArray as ABCExtensionArray, ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import overload

def array(data: Sequence[object] | AnyArrayLike, dtype: Dtype | None = None, copy: bool = True) -> ExtensionArray: ...
@overload
def extract_array(obj: Series | Index, extract_numpy: bool = ..., extract_range: bool = ...) -> ArrayLike: ...
@overload
def extract_array(obj: T, extract_numpy: bool = ..., extract_range: bool = ...) -> T | ArrayLike: ...
def ensure_wrapped_if_datetimelike(arr): ...
def sanitize_masked_array(data: ma.MaskedArray) -> np.ndarray: ...
def sanitize_array(data, index: Index | None, dtype: DtypeObj | None = None, copy: bool = False, *, allow_2d: bool = False) -> ArrayLike: ...
def range_to_ndarray(rng: range) -> np.ndarray: ...
