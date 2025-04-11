import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable, Iterable, Sequence
from pandas import DataFrame, Series
from pandas._typing import AnyAll, ArrayLike, Axis, DropKeep, DtypeObj, IgnoreRaise, IndexLabel, JoinHow, Level, NaPosition, ReindexMethod, Self, Shape, npt
from pandas.core.arrays import ExtensionArray
from pandas.core.base import IndexOpsMixin, PandasObject
from pandas.core.dtypes.missing import isna
from pandas.io.formats.printing import PrettyDict
from typing import Any, Callable, ClassVar, Literal, NoReturn, overload

__all__ = ['Index']

str_t = str

class Index(IndexOpsMixin, PandasObject):
    __pandas_priority__: int
    str: Incomplete
    def __new__(cls, data: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False, name: Incomplete | None = None, tupleize_cols: bool = True) -> Self: ...
    def is_(self, other) -> bool: ...
    def __len__(self) -> int: ...
    def __array__(self, dtype: Incomplete | None = None, copy: Incomplete | None = None) -> np.ndarray: ...
    def __array_ufunc__(self, ufunc: np.ufunc, method: str_t, *inputs, **kwargs): ...
    def __array_wrap__(self, result, context: Incomplete | None = None, return_scalar: bool = False): ...
    def dtype(self) -> DtypeObj: ...
    def ravel(self, order: str_t = 'C') -> Self: ...
    def view(self, cls: Incomplete | None = None): ...
    def astype(self, dtype, copy: bool = True): ...
    def take(self, indices, axis: Axis = 0, allow_fill: bool = True, fill_value: Incomplete | None = None, **kwargs) -> Self: ...
    def repeat(self, repeats, axis: None = None) -> Self: ...
    def copy(self, name: Hashable | None = None, deep: bool = False) -> Self: ...
    def __copy__(self, **kwargs) -> Self: ...
    def __deepcopy__(self, memo: Incomplete | None = None) -> Self: ...
    def format(self, name: bool = False, formatter: Callable | None = None, na_rep: str_t = 'NaN') -> list[str_t]: ...
    def to_flat_index(self) -> Self: ...
    def to_series(self, index: Incomplete | None = None, name: Hashable | None = None) -> Series: ...
    def to_frame(self, index: bool = True, name: Hashable = ...) -> DataFrame: ...
    @property
    def name(self) -> Hashable: ...
    @name.setter
    def name(self, value: Hashable) -> None: ...
    names: Incomplete
    @overload
    def set_names(self, names, *, level=..., inplace: Literal[False] = ...) -> Self: ...
    @overload
    def set_names(self, names, *, level=..., inplace: Literal[True]) -> None: ...
    @overload
    def set_names(self, names, *, level=..., inplace: bool = ...) -> Self | None: ...
    @overload
    def rename(self, name, *, inplace: Literal[False] = ...) -> Self: ...
    @overload
    def rename(self, name, *, inplace: Literal[True]) -> None: ...
    @property
    def nlevels(self) -> int: ...
    def sortlevel(self, level: Incomplete | None = None, ascending: bool | list[bool] = True, sort_remaining: Incomplete | None = None, na_position: NaPosition = 'first'): ...
    get_level_values: Incomplete
    def droplevel(self, level: IndexLabel = 0): ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    def is_unique(self) -> bool: ...
    @property
    def has_duplicates(self) -> bool: ...
    def is_boolean(self) -> bool: ...
    def is_integer(self) -> bool: ...
    def is_floating(self) -> bool: ...
    def is_numeric(self) -> bool: ...
    def is_object(self) -> bool: ...
    def is_categorical(self) -> bool: ...
    def is_interval(self) -> bool: ...
    def holds_integer(self) -> bool: ...
    def inferred_type(self) -> str_t: ...
    def __reduce__(self): ...
    def hasnans(self) -> bool: ...
    def isna(self) -> npt.NDArray[np.bool_]: ...
    isnull = isna
    def notna(self) -> npt.NDArray[np.bool_]: ...
    notnull = notna
    def fillna(self, value: Incomplete | None = None, downcast=...): ...
    def dropna(self, how: AnyAll = 'any') -> Self: ...
    def unique(self, level: Hashable | None = None) -> Self: ...
    def drop_duplicates(self, *, keep: DropKeep = 'first') -> Self: ...
    def duplicated(self, keep: DropKeep = 'first') -> npt.NDArray[np.bool_]: ...
    def __iadd__(self, other): ...
    def __nonzero__(self) -> NoReturn: ...
    __bool__ = __nonzero__
    def union(self, other, sort: Incomplete | None = None): ...
    def intersection(self, other, sort: bool = False): ...
    def difference(self, other, sort: Incomplete | None = None): ...
    def symmetric_difference(self, other, result_name: Incomplete | None = None, sort: Incomplete | None = None): ...
    def get_loc(self, key): ...
    def get_indexer(self, target, method: ReindexMethod | None = None, limit: int | None = None, tolerance: Incomplete | None = None) -> npt.NDArray[np.intp]: ...
    def reindex(self, target, method: ReindexMethod | None = None, level: Incomplete | None = None, limit: int | None = None, tolerance: float | None = None) -> tuple[Index, npt.NDArray[np.intp] | None]: ...
    @overload
    def join(self, other: Index, *, how: JoinHow = ..., level: Level = ..., return_indexers: Literal[True], sort: bool = ...) -> tuple[Index, npt.NDArray[np.intp] | None, npt.NDArray[np.intp] | None]: ...
    @overload
    def join(self, other: Index, *, how: JoinHow = ..., level: Level = ..., return_indexers: Literal[False] = ..., sort: bool = ...) -> Index: ...
    @overload
    def join(self, other: Index, *, how: JoinHow = ..., level: Level = ..., return_indexers: bool = ..., sort: bool = ...) -> Index | tuple[Index, npt.NDArray[np.intp] | None, npt.NDArray[np.intp] | None]: ...
    @property
    def values(self) -> ArrayLike: ...
    def array(self) -> ExtensionArray: ...
    def memory_usage(self, deep: bool = False) -> int: ...
    def where(self, cond, other: Incomplete | None = None) -> Index: ...
    def __contains__(self, key: Any) -> bool: ...
    __hash__: ClassVar[None]
    def __setitem__(self, key, value) -> None: ...
    def __getitem__(self, key): ...
    def append(self, other: Index | Sequence[Index]) -> Index: ...
    def putmask(self, mask, value) -> Index: ...
    def equals(self, other: Any) -> bool: ...
    def identical(self, other) -> bool: ...
    def asof(self, label): ...
    def asof_locs(self, where: Index, mask: npt.NDArray[np.bool_]) -> npt.NDArray[np.intp]: ...
    @overload
    def sort_values(self, *, return_indexer: Literal[False] = ..., ascending: bool = ..., na_position: NaPosition = ..., key: Callable | None = ...) -> Self: ...
    @overload
    def sort_values(self, *, return_indexer: Literal[True], ascending: bool = ..., na_position: NaPosition = ..., key: Callable | None = ...) -> tuple[Self, np.ndarray]: ...
    @overload
    def sort_values(self, *, return_indexer: bool = ..., ascending: bool = ..., na_position: NaPosition = ..., key: Callable | None = ...) -> Self | tuple[Self, np.ndarray]: ...
    def sort(self, *args, **kwargs) -> None: ...
    def shift(self, periods: int = 1, freq: Incomplete | None = None): ...
    def argsort(self, *args, **kwargs) -> npt.NDArray[np.intp]: ...
    def get_indexer_non_unique(self, target) -> tuple[npt.NDArray[np.intp], npt.NDArray[np.intp]]: ...
    def get_indexer_for(self, target) -> npt.NDArray[np.intp]: ...
    def groupby(self, values) -> PrettyDict[Hashable, np.ndarray]: ...
    def map(self, mapper, na_action: Literal['ignore'] | None = None): ...
    def isin(self, values, level: Incomplete | None = None) -> npt.NDArray[np.bool_]: ...
    def slice_indexer(self, start: Hashable | None = None, end: Hashable | None = None, step: int | None = None) -> slice: ...
    def get_slice_bound(self, label, side: Literal['left', 'right']) -> int: ...
    def slice_locs(self, start: Incomplete | None = None, end: Incomplete | None = None, step: Incomplete | None = None) -> tuple[int, int]: ...
    def delete(self, loc) -> Self: ...
    def insert(self, loc: int, item) -> Index: ...
    def drop(self, labels: Index | np.ndarray | Iterable[Hashable], errors: IgnoreRaise = 'raise') -> Index: ...
    def infer_objects(self, copy: bool = True) -> Index: ...
    def diff(self, periods: int = 1) -> Index: ...
    def round(self, decimals: int = 0) -> Self: ...
    def __abs__(self) -> Index: ...
    def __neg__(self) -> Index: ...
    def __pos__(self) -> Index: ...
    def __invert__(self) -> Index: ...
    def any(self, *args, **kwargs): ...
    def all(self, *args, **kwargs): ...
    def argmin(self, axis: Incomplete | None = None, skipna: bool = True, *args, **kwargs) -> int: ...
    def argmax(self, axis: Incomplete | None = None, skipna: bool = True, *args, **kwargs) -> int: ...
    def min(self, axis: Incomplete | None = None, skipna: bool = True, *args, **kwargs): ...
    def max(self, axis: Incomplete | None = None, skipna: bool = True, *args, **kwargs): ...
    @property
    def shape(self) -> Shape: ...
