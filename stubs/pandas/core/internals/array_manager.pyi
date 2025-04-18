import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable
from pandas._libs import NaT as NaT, lib as lib
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, QuantileInterpolation as QuantileInterpolation, Self as Self, npt as npt
from pandas.core.array_algos.quantile import quantile_compat as quantile_compat
from pandas.core.array_algos.take import take_1d as take_1d
from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, NumpyExtensionArray as NumpyExtensionArray, TimedeltaArray as TimedeltaArray
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array, sanitize_array as sanitize_array
from pandas.core.dtypes.astype import astype_array as astype_array, astype_array_safe as astype_array_safe
from pandas.core.dtypes.cast import ensure_dtype_can_hold_na as ensure_dtype_can_hold_na, find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar, np_find_common_type as np_find_common_type
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int, is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_integer as is_integer, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_timedelta64_ns_dtype as is_timedelta64_ns_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import array_equals as array_equals, isna as isna, na_value_for_dtype as na_value_for_dtype
from pandas.core.indexers import maybe_convert_indices as maybe_convert_indices, validate_indices as validate_indices
from pandas.core.indexes.api import Index as Index, ensure_index as ensure_index
from pandas.core.indexes.base import get_values_for_csv as get_values_for_csv
from pandas.core.internals.base import DataManager as DataManager, SingleDataManager as SingleDataManager, ensure_np_dtype as ensure_np_dtype, interleaved_dtype as interleaved_dtype
from pandas.core.internals.blocks import BlockPlacement as BlockPlacement, ensure_block_shape as ensure_block_shape, external_values as external_values, extract_pandas_array as extract_pandas_array, maybe_coerce_values as maybe_coerce_values, new_block as new_block
from pandas.core.internals.managers import make_na_array as make_na_array
from typing import Callable, Literal

class BaseArrayManager(DataManager):
    arrays: list[np.ndarray | ExtensionArray]
    def __init__(self, arrays: list[np.ndarray | ExtensionArray], axes: list[Index], verify_integrity: bool = True) -> None: ...
    def make_empty(self, axes: Incomplete | None = None) -> Self: ...
    @property
    def items(self) -> Index: ...
    @property
    def axes(self) -> list[Index]: ...
    @property
    def shape_proper(self) -> tuple[int, ...]: ...
    def set_axis(self, axis: AxisInt, new_labels: Index) -> None: ...
    def get_dtypes(self) -> npt.NDArray[np.object_]: ...
    def add_references(self, mgr: BaseArrayManager) -> None: ...
    def apply(self, f, align_keys: list[str] | None = None, **kwargs) -> Self: ...
    def apply_with_block(self, f, align_keys: Incomplete | None = None, **kwargs) -> Self: ...
    def setitem(self, indexer, value, warn: bool = True) -> Self: ...
    def diff(self, n: int) -> Self: ...
    def astype(self, dtype, copy: bool | None = False, errors: str = 'raise') -> Self: ...
    def convert(self, copy: bool | None) -> Self: ...
    def get_values_for_csv(self, *, float_format, date_format, decimal, na_rep: str = 'nan', quoting: Incomplete | None = None) -> Self: ...
    @property
    def any_extension_types(self) -> bool: ...
    @property
    def is_view(self) -> bool: ...
    @property
    def is_single_block(self) -> bool: ...
    def get_bool_data(self, copy: bool = False) -> Self: ...
    def get_numeric_data(self, copy: bool = False) -> Self: ...
    def copy(self, deep: bool | Literal['all'] | None = True) -> Self: ...
    def reindex_indexer(self, new_axis, indexer, axis: AxisInt, fill_value: Incomplete | None = None, allow_dups: bool = False, copy: bool | None = True, only_slice: bool = False, use_na_proxy: bool = False) -> Self: ...
    def take(self, indexer: npt.NDArray[np.intp], axis: AxisInt = 1, verify: bool = True) -> Self: ...

class ArrayManager(BaseArrayManager):
    @property
    def ndim(self) -> Literal[2]: ...
    arrays: Incomplete
    def __init__(self, arrays: list[np.ndarray | ExtensionArray], axes: list[Index], verify_integrity: bool = True) -> None: ...
    def fast_xs(self, loc: int) -> SingleArrayManager: ...
    def get_slice(self, slobj: slice, axis: AxisInt = 0) -> ArrayManager: ...
    def iget(self, i: int) -> SingleArrayManager: ...
    def iget_values(self, i: int) -> ArrayLike: ...
    @property
    def column_arrays(self) -> list[ArrayLike]: ...
    def iset(self, loc: int | slice | np.ndarray, value: ArrayLike, inplace: bool = False, refs: Incomplete | None = None) -> None: ...
    def column_setitem(self, loc: int, idx: int | slice | np.ndarray, value, inplace_only: bool = False) -> None: ...
    def insert(self, loc: int, item: Hashable, value: ArrayLike, refs: Incomplete | None = None) -> None: ...
    def idelete(self, indexer) -> ArrayManager: ...
    def grouped_reduce(self, func: Callable) -> Self: ...
    def reduce(self, func: Callable) -> Self: ...
    def operate_blockwise(self, other: ArrayManager, array_op) -> ArrayManager: ...
    def quantile(self, *, qs: Index, transposed: bool = False, interpolation: QuantileInterpolation = 'linear') -> ArrayManager: ...
    def unstack(self, unstacker, fill_value) -> ArrayManager: ...
    def as_array(self, dtype: Incomplete | None = None, copy: bool = False, na_value: object = ...) -> np.ndarray: ...
    @classmethod
    def concat_horizontal(cls, mgrs: list[Self], axes: list[Index]) -> Self: ...
    @classmethod
    def concat_vertical(cls, mgrs: list[Self], axes: list[Index]) -> Self: ...

class SingleArrayManager(BaseArrayManager, SingleDataManager):
    arrays: list[np.ndarray | ExtensionArray]
    @property
    def ndim(self) -> Literal[1]: ...
    def __init__(self, arrays: list[np.ndarray | ExtensionArray], axes: list[Index], verify_integrity: bool = True) -> None: ...
    def make_empty(self, axes: Incomplete | None = None) -> Self: ...
    @classmethod
    def from_array(cls, array, index) -> SingleArrayManager: ...
    @property
    def axes(self) -> list[Index]: ...
    @property
    def index(self) -> Index: ...
    @property
    def dtype(self): ...
    def external_values(self): ...
    def internal_values(self): ...
    def array_values(self): ...
    @property
    def is_single_block(self) -> bool: ...
    def fast_xs(self, loc: int) -> SingleArrayManager: ...
    def get_slice(self, slobj: slice, axis: AxisInt = 0) -> SingleArrayManager: ...
    def get_rows_with_mask(self, indexer: npt.NDArray[np.bool_]) -> SingleArrayManager: ...
    def apply(self, func, **kwargs) -> Self: ...
    def setitem(self, indexer, value, warn: bool = True) -> SingleArrayManager: ...
    def idelete(self, indexer) -> SingleArrayManager: ...
    def set_values(self, values: ArrayLike) -> None: ...
    def to_2d_mgr(self, columns: Index) -> ArrayManager: ...

class NullArrayProxy:
    ndim: int
    n: Incomplete
    def __init__(self, n: int) -> None: ...
    @property
    def shape(self) -> tuple[int]: ...
    def to_array(self, dtype: DtypeObj) -> ArrayLike: ...

def concat_arrays(to_concat: list) -> ArrayLike: ...
