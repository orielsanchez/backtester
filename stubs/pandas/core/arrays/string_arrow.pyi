import numpy as np
from _typeshed import Incomplete
from pandas import Series as Series
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, Dtype as Dtype, Scalar as Scalar, npt as npt
from pandas.compat import pa_version_under10p1 as pa_version_under10p1, pa_version_under13p0 as pa_version_under13p0
from pandas.core.arrays._arrow_string_mixins import ArrowStringArrayMixin as ArrowStringArrayMixin
from pandas.core.arrays.arrow import ArrowExtensionArray as ArrowExtensionArray
from pandas.core.arrays.arrow._arrow_utils import fallback_performancewarning as fallback_performancewarning
from pandas.core.arrays.boolean import BooleanDtype as BooleanDtype
from pandas.core.arrays.integer import Int64Dtype as Int64Dtype
from pandas.core.arrays.numeric import NumericDtype as NumericDtype
from pandas.core.arrays.string_ import BaseStringArray as BaseStringArray, StringDtype as StringDtype
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.ops import invalid_comparison as invalid_comparison
from pandas.core.strings.object_array import ObjectStringArrayMixin as ObjectStringArrayMixin
from pandas.util._exceptions import find_stack_level as find_stack_level

ArrowStringScalarOrNAT: Incomplete

class ArrowStringArray(ObjectStringArrayMixin, ArrowExtensionArray, BaseStringArray):
    def __init__(self, values) -> None: ...
    def __len__(self) -> int: ...
    @property
    def dtype(self) -> StringDtype: ...
    def insert(self, loc: int, item) -> ArrowStringArray: ...
    def isin(self, values: ArrayLike) -> npt.NDArray[np.bool_]: ...
    def astype(self, dtype, copy: bool = True): ...

class ArrowStringArrayNumpySemantics(ArrowStringArray):
    def __getattribute__(self, item): ...
    def value_counts(self, dropna: bool = True) -> Series: ...
    def insert(self, loc: int, item) -> ArrowStringArrayNumpySemantics: ...
