import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable, Iterator, Sequence
from pandas._config.config import option_context as option_context
from pandas._libs import Timestamp as Timestamp, lib as lib
from pandas._libs.algos import rank_1d as rank_1d
from pandas._libs.missing import NA as NA
from pandas._typing import AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, Axis as Axis, AxisInt as AxisInt, DtypeObj as DtypeObj, FillnaOptions as FillnaOptions, IndexLabel as IndexLabel, NDFrameT as NDFrameT, PositionalIndexer as PositionalIndexer, RandomState as RandomState, Scalar as Scalar, T as T, npt as npt
from pandas.core import algorithms as algorithms, sample as sample
from pandas.core._numba import executor as executor
from pandas.core.apply import warn_alias_replacement as warn_alias_replacement
from pandas.core.arrays import ArrowExtensionArray as ArrowExtensionArray, BaseMaskedArray as BaseMaskedArray, Categorical as Categorical, ExtensionArray as ExtensionArray, FloatingArray as FloatingArray, IntegerArray as IntegerArray, SparseArray as SparseArray
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.arrays.string_arrow import ArrowStringArray as ArrowStringArray, ArrowStringArrayNumpySemantics as ArrowStringArrayNumpySemantics
from pandas.core.base import PandasObject as PandasObject, SelectionMixin as SelectionMixin
from pandas.core.dtypes.cast import coerce_indexer_dtype as coerce_indexer_dtype, ensure_dtype_can_hold_na as ensure_dtype_can_hold_na
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_float_dtype as is_float_dtype, is_hashable as is_hashable, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.missing import isna as isna, na_value_for_dtype as na_value_for_dtype, notna as notna
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby import base as base, numba_ as numba_, ops as ops
from pandas.core.groupby.grouper import get_grouper as get_grouper
from pandas.core.groupby.indexing import GroupByIndexingMixin as GroupByIndexingMixin, GroupByNthSelector as GroupByNthSelector
from pandas.core.indexes.api import CategoricalIndex as CategoricalIndex, Index as Index, MultiIndex as MultiIndex, RangeIndex as RangeIndex, default_index as default_index
from pandas.core.internals.blocks import ensure_block_shape as ensure_block_shape
from pandas.core.resample import Resampler as Resampler
from pandas.core.series import Series as Series
from pandas.core.sorting import get_group_index_sorter as get_group_index_sorter
from pandas.core.util.numba_ import get_jit_arguments as get_jit_arguments, maybe_use_numba as maybe_use_numba
from pandas.core.window import ExpandingGroupby as ExpandingGroupby, ExponentialMovingWindowGroupby as ExponentialMovingWindowGroupby, RollingGroupby as RollingGroupby
from pandas.errors import AbstractMethodError as AbstractMethodError, DataError as DataError
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Callable, Literal, TypeVar

class GroupByPlot(PandasObject):
    def __init__(self, groupby: GroupBy) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __getattr__(self, name: str): ...

class BaseGroupBy(PandasObject, SelectionMixin[NDFrameT], GroupByIndexingMixin):
    axis: AxisInt
    keys: _KeysArgType | None
    level: IndexLabel | None
    group_keys: bool
    def __len__(self) -> int: ...
    @property
    def grouper(self) -> ops.BaseGrouper: ...
    @property
    def groups(self) -> dict[Hashable, np.ndarray]: ...
    @property
    def ngroups(self) -> int: ...
    @property
    def indices(self) -> dict[Hashable, npt.NDArray[np.intp]]: ...
    def pipe(self, func: Callable[..., T] | tuple[Callable[..., T], str], *args, **kwargs) -> T: ...
    def get_group(self, name, obj: Incomplete | None = None) -> DataFrame | Series: ...
    def __iter__(self) -> Iterator[tuple[Hashable, NDFrameT]]: ...
OutputFrameOrSeries = TypeVar('OutputFrameOrSeries', bound=NDFrame)

class GroupBy(BaseGroupBy[NDFrameT]):
    as_index: bool
    level: Incomplete
    keys: Incomplete
    sort: Incomplete
    group_keys: Incomplete
    dropna: Incomplete
    observed: Incomplete
    obj: Incomplete
    axis: Incomplete
    exclusions: Incomplete
    def __init__(self, obj: NDFrameT, keys: _KeysArgType | None = None, axis: Axis = 0, level: IndexLabel | None = None, grouper: ops.BaseGrouper | None = None, exclusions: frozenset[Hashable] | None = None, selection: IndexLabel | None = None, as_index: bool = True, sort: bool = True, group_keys: bool = True, observed: bool | lib.NoDefault = ..., dropna: bool = True) -> None: ...
    def __getattr__(self, attr: str): ...
    def apply(self, func, *args, include_groups: bool = True, **kwargs) -> NDFrameT: ...
    def any(self, skipna: bool = True) -> NDFrameT: ...
    def all(self, skipna: bool = True) -> NDFrameT: ...
    def count(self) -> NDFrameT: ...
    def mean(self, numeric_only: bool = False, engine: Literal['cython', 'numba'] | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def median(self, numeric_only: bool = False) -> NDFrameT: ...
    def std(self, ddof: int = 1, engine: Literal['cython', 'numba'] | None = None, engine_kwargs: dict[str, bool] | None = None, numeric_only: bool = False): ...
    def var(self, ddof: int = 1, engine: Literal['cython', 'numba'] | None = None, engine_kwargs: dict[str, bool] | None = None, numeric_only: bool = False): ...
    def sem(self, ddof: int = 1, numeric_only: bool = False) -> NDFrameT: ...
    def size(self) -> DataFrame | Series: ...
    def sum(self, numeric_only: bool = False, min_count: int = 0, engine: Literal['cython', 'numba'] | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def prod(self, numeric_only: bool = False, min_count: int = 0) -> NDFrameT: ...
    def min(self, numeric_only: bool = False, min_count: int = -1, engine: Literal['cython', 'numba'] | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def max(self, numeric_only: bool = False, min_count: int = -1, engine: Literal['cython', 'numba'] | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def first(self, numeric_only: bool = False, min_count: int = -1, skipna: bool = True) -> NDFrameT: ...
    def last(self, numeric_only: bool = False, min_count: int = -1, skipna: bool = True) -> NDFrameT: ...
    def ohlc(self) -> DataFrame: ...
    def describe(self, percentiles: Incomplete | None = None, include: Incomplete | None = None, exclude: Incomplete | None = None) -> NDFrameT: ...
    def resample(self, rule, *args, include_groups: bool = True, **kwargs) -> Resampler: ...
    def rolling(self, *args, **kwargs) -> RollingGroupby: ...
    def expanding(self, *args, **kwargs) -> ExpandingGroupby: ...
    def ewm(self, *args, **kwargs) -> ExponentialMovingWindowGroupby: ...
    def ffill(self, limit: int | None = None): ...
    def bfill(self, limit: int | None = None): ...
    @property
    def nth(self) -> GroupByNthSelector: ...
    def quantile(self, q: float | AnyArrayLike = 0.5, interpolation: str = 'linear', numeric_only: bool = False): ...
    def ngroup(self, ascending: bool = True): ...
    def cumcount(self, ascending: bool = True): ...
    def rank(self, method: str = 'average', ascending: bool = True, na_option: str = 'keep', pct: bool = False, axis: AxisInt | lib.NoDefault = ...) -> NDFrameT: ...
    def cumprod(self, axis: Axis | lib.NoDefault = ..., *args, **kwargs) -> NDFrameT: ...
    def cumsum(self, axis: Axis | lib.NoDefault = ..., *args, **kwargs) -> NDFrameT: ...
    def cummin(self, axis: AxisInt | lib.NoDefault = ..., numeric_only: bool = False, **kwargs) -> NDFrameT: ...
    def cummax(self, axis: AxisInt | lib.NoDefault = ..., numeric_only: bool = False, **kwargs) -> NDFrameT: ...
    def shift(self, periods: int | Sequence[int] = 1, freq: Incomplete | None = None, axis: Axis | lib.NoDefault = ..., fill_value=..., suffix: str | None = None): ...
    def diff(self, periods: int = 1, axis: AxisInt | lib.NoDefault = ...) -> NDFrameT: ...
    def pct_change(self, periods: int = 1, fill_method: FillnaOptions | None | lib.NoDefault = ..., limit: int | None | lib.NoDefault = ..., freq: Incomplete | None = None, axis: Axis | lib.NoDefault = ...): ...
    def head(self, n: int = 5) -> NDFrameT: ...
    def tail(self, n: int = 5) -> NDFrameT: ...
    def sample(self, n: int | None = None, frac: float | None = None, replace: bool = False, weights: Sequence | Series | None = None, random_state: RandomState | None = None): ...

def get_groupby(obj: NDFrame, by: _KeysArgType | None = None, axis: AxisInt = 0, grouper: ops.BaseGrouper | None = None, group_keys: bool = True) -> GroupBy: ...
