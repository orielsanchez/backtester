import numpy as np
from _typeshed import Incomplete
from collections.abc import Iterator
from pandas import DataFrame as DataFrame, Index as Index, Series as Series
from pandas._config import get_option as get_option
from pandas._libs import NaT as NaT, lib as lib
from pandas._libs.arrays import NDArrayBacked as NDArrayBacked
from pandas._typing import ArrayLike as ArrayLike, AstypeArg as AstypeArg, AxisInt as AxisInt, Dtype as Dtype, DtypeObj as DtypeObj, NpDtype as NpDtype, Ordered as Ordered, Self as Self, Shape as Shape, SortKind as SortKind, npt as npt
from pandas.core import algorithms as algorithms, arraylike as arraylike, ops as ops
from pandas.core.accessor import PandasDelegate as PandasDelegate, delegate_names as delegate_names
from pandas.core.algorithms import factorize as factorize, take_nd as take_nd
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray, ravel_compat as ravel_compat
from pandas.core.base import ExtensionArray as ExtensionArray, NoNewAttributesMixin as NoNewAttributesMixin, PandasObject as PandasObject
from pandas.core.construction import extract_array as extract_array, sanitize_array as sanitize_array
from pandas.core.dtypes.cast import coerce_indexer_dtype as coerce_indexer_dtype, find_common_type as find_common_type
from pandas.core.dtypes.common import ensure_int64 as ensure_int64, ensure_platform_int as ensure_platform_int, is_any_real_numeric_dtype as is_any_real_numeric_dtype, is_bool_dtype as is_bool_dtype, is_dict_like as is_dict_like, is_hashable as is_hashable, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_scalar as is_scalar, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype as ArrowDtype, CategoricalDtype as CategoricalDtype, CategoricalDtypeType as CategoricalDtypeType, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna
from pandas.core.ops.common import unpack_zerodim_and_defer as unpack_zerodim_and_defer
from pandas.core.sorting import nargsort as nargsort
from pandas.core.strings.object_array import ObjectStringArrayMixin as ObjectStringArrayMixin
from pandas.io.formats import console as console
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Literal, overload

def contains(cat, key, container) -> bool: ...

class Categorical(NDArrayBackedExtensionArray, PandasObject, ObjectStringArrayMixin):
    __array_priority__: int
    def __init__(self, values, categories: Incomplete | None = None, ordered: Incomplete | None = None, dtype: Dtype | None = None, fastpath: bool | lib.NoDefault = ..., copy: bool = True) -> None: ...
    @property
    def dtype(self) -> CategoricalDtype: ...
    @overload
    def astype(self, dtype: npt.DTypeLike, copy: bool = ...) -> np.ndarray: ...
    @overload
    def astype(self, dtype: ExtensionDtype, copy: bool = ...) -> ExtensionArray: ...
    @overload
    def astype(self, dtype: AstypeArg, copy: bool = ...) -> ArrayLike: ...
    def to_list(self): ...
    @classmethod
    def from_codes(cls, codes, categories: Incomplete | None = None, ordered: Incomplete | None = None, dtype: Dtype | None = None, validate: bool = True) -> Self: ...
    @property
    def categories(self) -> Index: ...
    @property
    def ordered(self) -> Ordered: ...
    @property
    def codes(self) -> np.ndarray: ...
    def set_ordered(self, value: bool) -> Self: ...
    def as_ordered(self) -> Self: ...
    def as_unordered(self) -> Self: ...
    def set_categories(self, new_categories, ordered: Incomplete | None = None, rename: bool = False): ...
    def rename_categories(self, new_categories) -> Self: ...
    def reorder_categories(self, new_categories, ordered: Incomplete | None = None) -> Self: ...
    def add_categories(self, new_categories) -> Self: ...
    def remove_categories(self, removals) -> Self: ...
    def remove_unused_categories(self) -> Self: ...
    def map(self, mapper, na_action: Literal['ignore'] | None | lib.NoDefault = ...): ...
    __eq__: Incomplete
    __ne__: Incomplete
    __lt__: Incomplete
    __gt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    def __array__(self, dtype: NpDtype | None = None, copy: bool | None = None) -> np.ndarray: ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs): ...
    @property
    def nbytes(self) -> int: ...
    def memory_usage(self, deep: bool = False) -> int: ...
    def isna(self) -> npt.NDArray[np.bool_]: ...
    isnull = isna
    def notna(self) -> npt.NDArray[np.bool_]: ...
    notnull = notna
    def value_counts(self, dropna: bool = True) -> Series: ...
    def check_for_ordered(self, op) -> None: ...
    def argsort(self, *, ascending: bool = True, kind: SortKind = 'quicksort', **kwargs): ...
    @overload
    def sort_values(self, *, inplace: Literal[False] = ..., ascending: bool = ..., na_position: str = ...) -> Self: ...
    @overload
    def sort_values(self, *, inplace: Literal[True], ascending: bool = ..., na_position: str = ...) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __contains__(self, key) -> bool: ...
    def min(self, *, skipna: bool = True, **kwargs): ...
    def max(self, *, skipna: bool = True, **kwargs): ...
    def unique(self) -> Self: ...
    def equals(self, other: object) -> bool: ...
    def describe(self) -> DataFrame: ...
    def isin(self, values: ArrayLike) -> npt.NDArray[np.bool_]: ...

class CategoricalAccessor(PandasDelegate, PandasObject, NoNewAttributesMixin):
    def __init__(self, data) -> None: ...
    @property
    def codes(self) -> Series: ...

def recode_for_categories(codes: np.ndarray, old_categories, new_categories, copy: bool = True) -> np.ndarray: ...
def factorize_from_iterable(values) -> tuple[np.ndarray, Index]: ...
def factorize_from_iterables(iterables) -> tuple[list[np.ndarray], list[Index]]: ...
