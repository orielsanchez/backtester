import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable, Sequence
from pandas import ArrowDtype as ArrowDtype, Categorical as Categorical, DataFrame as DataFrame, Index as Index, MultiIndex as MultiIndex, Series as Series
from pandas._libs import Timedelta as Timedelta, lib as lib
from pandas._libs.lib import is_range_indexer as is_range_indexer
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, IndexLabel as IndexLabel, JoinHow as JoinHow, MergeHow as MergeHow, Shape as Shape, Suffixes as Suffixes, npt as npt
from pandas.core import groupby as groupby
from pandas.core.arrays import ArrowExtensionArray as ArrowExtensionArray, BaseMaskedArray as BaseMaskedArray, DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.cast import find_common_type as find_common_type
from pandas.core.dtypes.common import ensure_int64 as ensure_int64, ensure_object as ensure_object, is_bool as is_bool, is_bool_dtype as is_bool_dtype, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_number as is_number, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_string_dtype as is_string_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, DatetimeTZDtype as DatetimeTZDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexes.api import default_index as default_index
from pandas.core.indexes.frozen import FrozenList as FrozenList
from pandas.core.sorting import get_group_index as get_group_index, is_int64_overflow_possible as is_int64_overflow_possible
from pandas.errors import MergeError as MergeError
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Literal

def merge(left: DataFrame | Series, right: DataFrame | Series, how: MergeHow = 'inner', on: IndexLabel | AnyArrayLike | None = None, left_on: IndexLabel | AnyArrayLike | None = None, right_on: IndexLabel | AnyArrayLike | None = None, left_index: bool = False, right_index: bool = False, sort: bool = False, suffixes: Suffixes = ('_x', '_y'), copy: bool | None = None, indicator: str | bool = False, validate: str | None = None) -> DataFrame: ...
def merge_ordered(left: DataFrame | Series, right: DataFrame | Series, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_by: Incomplete | None = None, right_by: Incomplete | None = None, fill_method: str | None = None, suffixes: Suffixes = ('_x', '_y'), how: JoinHow = 'outer') -> DataFrame: ...
def merge_asof(left: DataFrame | Series, right: DataFrame | Series, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, by: Incomplete | None = None, left_by: Incomplete | None = None, right_by: Incomplete | None = None, suffixes: Suffixes = ('_x', '_y'), tolerance: int | Timedelta | None = None, allow_exact_matches: bool = True, direction: str = 'backward') -> DataFrame: ...

class _MergeOperation:
    how: JoinHow | Literal['asof']
    on: IndexLabel | None
    left_on: Sequence[Hashable | AnyArrayLike]
    right_on: Sequence[Hashable | AnyArrayLike]
    left_index: bool
    right_index: bool
    sort: bool
    suffixes: Suffixes
    copy: bool
    indicator: str | bool
    validate: str | None
    join_names: list[Hashable]
    right_join_keys: list[ArrayLike]
    left_join_keys: list[ArrayLike]
    left: Incomplete
    right: Incomplete
    def __init__(self, left: DataFrame | Series, right: DataFrame | Series, how: JoinHow | Literal['asof'] = 'inner', on: IndexLabel | AnyArrayLike | None = None, left_on: IndexLabel | AnyArrayLike | None = None, right_on: IndexLabel | AnyArrayLike | None = None, left_index: bool = False, right_index: bool = False, sort: bool = True, suffixes: Suffixes = ('_x', '_y'), indicator: str | bool = False, validate: str | None = None) -> None: ...
    def get_result(self, copy: bool | None = True) -> DataFrame: ...

def get_join_indexers(left_keys: list[ArrayLike], right_keys: list[ArrayLike], sort: bool = False, how: JoinHow = 'inner') -> tuple[npt.NDArray[np.intp] | None, npt.NDArray[np.intp] | None]: ...
def get_join_indexers_non_unique(left: ArrayLike, right: ArrayLike, sort: bool = False, how: JoinHow = 'inner') -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]: ...
def restore_dropped_levels_multijoin(left: MultiIndex, right: MultiIndex, dropped_level_names, join_index: Index, lindexer: npt.NDArray[np.intp], rindexer: npt.NDArray[np.intp]) -> tuple[FrozenList, FrozenList, FrozenList]: ...

class _OrderedMerge(_MergeOperation):
    fill_method: Incomplete
    def __init__(self, left: DataFrame | Series, right: DataFrame | Series, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, suffixes: Suffixes = ('_x', '_y'), fill_method: str | None = None, how: JoinHow | Literal['asof'] = 'outer') -> None: ...
    def get_result(self, copy: bool | None = True) -> DataFrame: ...

class _AsOfMerge(_OrderedMerge):
    by: Incomplete
    left_by: Incomplete
    right_by: Incomplete
    tolerance: Incomplete
    allow_exact_matches: Incomplete
    direction: Incomplete
    def __init__(self, left: DataFrame | Series, right: DataFrame | Series, on: IndexLabel | None = None, left_on: IndexLabel | None = None, right_on: IndexLabel | None = None, left_index: bool = False, right_index: bool = False, by: Incomplete | None = None, left_by: Incomplete | None = None, right_by: Incomplete | None = None, suffixes: Suffixes = ('_x', '_y'), how: Literal['asof'] = 'asof', tolerance: Incomplete | None = None, allow_exact_matches: bool = True, direction: str = 'backward') -> None: ...
