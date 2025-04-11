import numpy as np
from collections.abc import Sequence
from pandas._config import using_pyarrow_string_dtype as using_pyarrow_string_dtype
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, Manager as Manager, npt as npt
from pandas.core import algorithms as algorithms
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, extract_array as extract_array, range_to_ndarray as range_to_ndarray, sanitize_array as sanitize_array
from pandas.core.dtypes.astype import astype_is_view as astype_is_view
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, dict_compat as dict_compat, maybe_cast_to_datetime as maybe_cast_to_datetime, maybe_convert_platform as maybe_convert_platform, maybe_infer_to_datetimelike as maybe_infer_to_datetimelike
from pandas.core.dtypes.common import is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_named_tuple as is_named_tuple, is_object_dtype as is_object_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.indexes.api import DatetimeIndex as DatetimeIndex, Index as Index, TimedeltaIndex as TimedeltaIndex, default_index as default_index, ensure_index as ensure_index, get_objs_combined_axis as get_objs_combined_axis, union_indexes as union_indexes
from pandas.core.internals.array_manager import ArrayManager as ArrayManager, SingleArrayManager as SingleArrayManager
from pandas.core.internals.blocks import BlockPlacement as BlockPlacement, ensure_block_shape as ensure_block_shape, new_block as new_block, new_block_2d as new_block_2d
from pandas.core.internals.managers import BlockManager as BlockManager, SingleBlockManager as SingleBlockManager, create_block_manager_from_blocks as create_block_manager_from_blocks, create_block_manager_from_column_arrays as create_block_manager_from_column_arrays

def arrays_to_mgr(arrays, columns: Index, index, *, dtype: DtypeObj | None = None, verify_integrity: bool = True, typ: str | None = None, consolidate: bool = True) -> Manager: ...
def rec_array_to_mgr(data: np.rec.recarray | np.ndarray, index, columns, dtype: DtypeObj | None, copy: bool, typ: str) -> Manager: ...
def mgr_to_mgr(mgr, typ: str, copy: bool = True) -> Manager: ...
def ndarray_to_mgr(values, index, columns, dtype: DtypeObj | None, copy: bool, typ: str) -> Manager: ...
def dict_to_mgr(data: dict, index, columns, *, dtype: DtypeObj | None = None, typ: str = 'block', copy: bool = True) -> Manager: ...
def nested_data_to_arrays(data: Sequence, columns: Index | None, index: Index | None, dtype: DtypeObj | None) -> tuple[list[ArrayLike], Index, Index]: ...
def treat_as_nested(data) -> bool: ...
def reorder_arrays(arrays: list[ArrayLike], arr_columns: Index, columns: Index | None, length: int) -> tuple[list[ArrayLike], Index]: ...
def dataclasses_to_dicts(data): ...
def to_arrays(data, columns: Index | None, dtype: DtypeObj | None = None) -> tuple[list[ArrayLike], Index]: ...
def convert_object_array(content: list[npt.NDArray[np.object_]], dtype: DtypeObj | None, dtype_backend: str = 'numpy', coerce_float: bool = False) -> list[ArrayLike]: ...
