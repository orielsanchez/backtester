import numpy as np
from _typeshed import Incomplete
from collections.abc import Iterator, Sequence
from pandas import Index as Index
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, AstypeArg as AstypeArg, AxisInt as AxisInt, Dtype as Dtype, DtypeObj as DtypeObj, FillnaOptions as FillnaOptions, InterpolateOptions as InterpolateOptions, NumpySorter as NumpySorter, NumpyValueArrayLike as NumpyValueArrayLike, PositionalIndexer as PositionalIndexer, ScalarIndexer as ScalarIndexer, Self as Self, SequenceIndexer as SequenceIndexer, Shape as Shape, SortKind as SortKind, TakeIndexer as TakeIndexer, npt as npt
from pandas.compat import set_function_name as set_function_name
from pandas.core import arraylike as arraylike, missing as missing, roperator as roperator
from pandas.core.algorithms import duplicated as duplicated, factorize_array as factorize_array, isin as isin, map_array as map_array, mode as mode, rank as rank, unique as unique
from pandas.core.array_algos.quantile import quantile_with_mask as quantile_with_mask
from pandas.core.dtypes.cast import maybe_cast_pointwise_result as maybe_cast_pointwise_result
from pandas.core.dtypes.common import is_list_like as is_list_like, is_scalar as is_scalar, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.core.sorting import nargminmax as nargminmax, nargsort as nargsort
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg, validate_fillna_kwargs as validate_fillna_kwargs, validate_insert_loc as validate_insert_loc
from typing import Any, ClassVar, Literal, overload

class ExtensionArray:
    __pandas_priority__: int
    @overload
    def __getitem__(self, item: ScalarIndexer) -> Any: ...
    @overload
    def __getitem__(self, item: SequenceIndexer) -> Self: ...
    def __setitem__(self, key, value) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __contains__(self, item: object) -> bool | np.bool_: ...
    def __eq__(self, other: object) -> ArrayLike: ...
    def __ne__(self, other: object) -> ArrayLike: ...
    def to_numpy(self, dtype: npt.DTypeLike | None = None, copy: bool = False, na_value: object = ...) -> np.ndarray: ...
    @property
    def dtype(self) -> ExtensionDtype: ...
    @property
    def shape(self) -> Shape: ...
    @property
    def size(self) -> int: ...
    @property
    def ndim(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    @overload
    def astype(self, dtype: npt.DTypeLike, copy: bool = ...) -> np.ndarray: ...
    @overload
    def astype(self, dtype: ExtensionDtype, copy: bool = ...) -> ExtensionArray: ...
    @overload
    def astype(self, dtype: AstypeArg, copy: bool = ...) -> ArrayLike: ...
    def isna(self) -> np.ndarray | ExtensionArraySupportsAnyAll: ...
    def argsort(self, *, ascending: bool = True, kind: SortKind = 'quicksort', na_position: str = 'last', **kwargs) -> np.ndarray: ...
    def argmin(self, skipna: bool = True) -> int: ...
    def argmax(self, skipna: bool = True) -> int: ...
    def interpolate(self, *, method: InterpolateOptions, axis: int, index: Index, limit, limit_direction, limit_area, copy: bool, **kwargs) -> Self: ...
    def fillna(self, value: object | ArrayLike | None = None, method: FillnaOptions | None = None, limit: int | None = None, copy: bool = True) -> Self: ...
    def dropna(self) -> Self: ...
    def duplicated(self, keep: Literal['first', 'last', False] = 'first') -> npt.NDArray[np.bool_]: ...
    def shift(self, periods: int = 1, fill_value: object = None) -> ExtensionArray: ...
    def unique(self) -> Self: ...
    def searchsorted(self, value: NumpyValueArrayLike | ExtensionArray, side: Literal['left', 'right'] = 'left', sorter: NumpySorter | None = None) -> npt.NDArray[np.intp] | np.intp: ...
    def equals(self, other: object) -> bool: ...
    def isin(self, values: ArrayLike) -> npt.NDArray[np.bool_]: ...
    def factorize(self, use_na_sentinel: bool = True) -> tuple[np.ndarray, ExtensionArray]: ...
    def repeat(self, repeats: int | Sequence[int], axis: AxisInt | None = None) -> Self: ...
    def take(self, indices: TakeIndexer, *, allow_fill: bool = False, fill_value: Any = None) -> Self: ...
    def copy(self) -> Self: ...
    def view(self, dtype: Dtype | None = None) -> ArrayLike: ...
    def transpose(self, *axes: int) -> ExtensionArray: ...
    @property
    def T(self) -> ExtensionArray: ...
    def ravel(self, order: Literal['C', 'F', 'A', 'K'] | None = 'C') -> ExtensionArray: ...
    __hash__: ClassVar[None]
    def tolist(self) -> list: ...
    def delete(self, loc: PositionalIndexer) -> Self: ...
    def insert(self, loc: int, item) -> Self: ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str, *inputs, **kwargs): ...
    def map(self, mapper, na_action: Incomplete | None = None): ...

class ExtensionArraySupportsAnyAll(ExtensionArray):
    def any(self, *, skipna: bool = True) -> bool: ...
    def all(self, *, skipna: bool = True) -> bool: ...

class ExtensionOpsMixin: ...
class ExtensionScalarOpsMixin(ExtensionOpsMixin): ...
