import datetime
import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable, Iterable, Mapping, Sequence
from pandas._config import get_option as get_option, using_copy_on_write as using_copy_on_write, warn_copy_on_write as warn_copy_on_write
from pandas._libs import lib as lib, properties as properties
from pandas._libs.hashtable import duplicated as duplicated
from pandas._libs.internals import BlockValuesRefs as BlockValuesRefs
from pandas._libs.lib import is_range_indexer as is_range_indexer
from pandas._typing import AggFuncType as AggFuncType, AnyAll as AnyAll, AnyArrayLike as AnyArrayLike, ArrayLike as ArrayLike, Axes as Axes, Axis as Axis, AxisInt as AxisInt, ColspaceArgType as ColspaceArgType, CompressionOptions as CompressionOptions, CorrelationMethod as CorrelationMethod, DropKeep as DropKeep, Dtype as Dtype, DtypeObj as DtypeObj, FilePath as FilePath, FloatFormatType as FloatFormatType, FormattersType as FormattersType, Frequency as Frequency, FromDictOrient as FromDictOrient, IgnoreRaise as IgnoreRaise, IndexKeyFunc as IndexKeyFunc, IndexLabel as IndexLabel, JoinValidate as JoinValidate, Level as Level, MergeHow as MergeHow, MergeValidate as MergeValidate, MutableMappingT as MutableMappingT, NaAction as NaAction, NaPosition as NaPosition, NsmallestNlargestKeep as NsmallestNlargestKeep, PythonFuncType as PythonFuncType, QuantileInterpolation as QuantileInterpolation, ReadBuffer as ReadBuffer, ReindexMethod as ReindexMethod, Renamer as Renamer, Scalar as Scalar, Self as Self, SequenceNotStr as SequenceNotStr, SortKind as SortKind, StorageOptions as StorageOptions, Suffixes as Suffixes, ToGbqIfexist as ToGbqIfexist, ToStataByteorder as ToStataByteorder, ToTimestampHow as ToTimestampHow, UpdateJoin as UpdateJoin, ValueKeyFunc as ValueKeyFunc, WriteBuffer as WriteBuffer, XMLParsers as XMLParsers, npt as npt
from pandas.compat import PYPY as PYPY
from pandas.compat._constants import REF_COUNT as REF_COUNT
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core import algorithms as algorithms, nanops as nanops, ops as ops, roperator as roperator
from pandas.core.accessor import CachedAccessor as CachedAccessor
from pandas.core.apply import reconstruct_and_relabel_result as reconstruct_and_relabel_result
from pandas.core.array_algos.take import take_2d_multi as take_2d_multi
from pandas.core.arraylike import OpsMixin as OpsMixin
from pandas.core.arrays import BaseMaskedArray as BaseMaskedArray, DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.sparse import SparseFrameAccessor as SparseFrameAccessor
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike, sanitize_array as sanitize_array, sanitize_masked_array as sanitize_masked_array
from pandas.core.dtypes.cast import LossySetitemError as LossySetitemError, can_hold_element as can_hold_element, construct_1d_arraylike_from_scalar as construct_1d_arraylike_from_scalar, construct_2d_arraylike_from_scalar as construct_2d_arraylike_from_scalar, find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar, invalidate_string_dtypes as invalidate_string_dtypes, maybe_box_native as maybe_box_native, maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import infer_dtype_from_object as infer_dtype_from_object, is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_array_like as is_array_like, is_bool_dtype as is_bool_dtype, is_dataclass as is_dataclass, is_dict_like as is_dict_like, is_float as is_float, is_float_dtype as is_float_dtype, is_hashable as is_hashable, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_iterator as is_iterator, is_list_like as is_list_like, is_scalar as is_scalar, is_sequence as is_sequence, needs_i8_conversion as needs_i8_conversion, pandas_dtype as pandas_dtype
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.dtypes import ArrowDtype as ArrowDtype, BaseMaskedDtype as BaseMaskedDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.generic import NDFrame as NDFrame, make_doc as make_doc
from pandas.core.groupby.generic import DataFrameGroupBy as DataFrameGroupBy
from pandas.core.indexers import check_key_length as check_key_length
from pandas.core.indexes.api import DatetimeIndex as DatetimeIndex, Index as Index, PeriodIndex as PeriodIndex, default_index as default_index, ensure_index as ensure_index, ensure_index_from_sequences as ensure_index_from_sequences
from pandas.core.indexes.multi import MultiIndex as MultiIndex, maybe_droplevels as maybe_droplevels
from pandas.core.indexing import check_bool_indexer as check_bool_indexer, check_dict_or_set_indexers as check_dict_or_set_indexers
from pandas.core.interchange.dataframe_protocol import DataFrame as DataFrameXchg
from pandas.core.internals import ArrayManager as ArrayManager, BlockManager as BlockManager, SingleDataManager as SingleDataManager
from pandas.core.internals.construction import arrays_to_mgr as arrays_to_mgr, dataclasses_to_dicts as dataclasses_to_dicts, dict_to_mgr as dict_to_mgr, mgr_to_mgr as mgr_to_mgr, ndarray_to_mgr as ndarray_to_mgr, nested_data_to_arrays as nested_data_to_arrays, rec_array_to_mgr as rec_array_to_mgr, reorder_arrays as reorder_arrays, to_arrays as to_arrays, treat_as_nested as treat_as_nested
from pandas.core.methods import selectn as selectn
from pandas.core.reshape.melt import melt as melt
from pandas.core.series import Series as Series
from pandas.core.sorting import get_group_index as get_group_index, lexsort_indexer as lexsort_indexer, nargsort as nargsort
from pandas.errors import ChainedAssignmentError as ChainedAssignmentError, InvalidIndexError as InvalidIndexError
from pandas.io.common import get_handle as get_handle
from pandas.io.formats import console as console, format as fmt
from pandas.io.formats.info import DataFrameInfo as DataFrameInfo, INFO_DOCSTRING as INFO_DOCSTRING, frame_sub_kwargs as frame_sub_kwargs
from pandas.io.formats.style import Styler as Styler
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, deprecate_nonkeyword_arguments as deprecate_nonkeyword_arguments, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level, rewrite_warning as rewrite_warning
from pandas.util._validators import validate_ascending as validate_ascending, validate_bool_kwarg as validate_bool_kwarg, validate_percentile as validate_percentile
from typing import Any, Callable, Literal, overload

class DataFrame(NDFrame, OpsMixin):
    __pandas_priority__: int
    def __init__(self, data: Incomplete | None = None, index: Axes | None = None, columns: Axes | None = None, dtype: Dtype | None = None, copy: bool | None = None) -> None: ...
    def __dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True) -> DataFrameXchg: ...
    def __dataframe_consortium_standard__(self, *, api_version: str | None = None) -> Any: ...
    def __arrow_c_stream__(self, requested_schema: Incomplete | None = None): ...
    @property
    def axes(self) -> list[Index]: ...
    @property
    def shape(self) -> tuple[int, int]: ...
    @overload
    def to_string(self, buf: None = ..., columns: Axes | None = ..., col_space: int | list[int] | dict[Hashable, int] | None = ..., header: bool | SequenceNotStr[str] = ..., index: bool = ..., na_rep: str = ..., formatters: fmt.FormattersType | None = ..., float_format: fmt.FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool = ..., decimal: str = ..., line_width: int | None = ..., min_rows: int | None = ..., max_colwidth: int | None = ..., encoding: str | None = ...) -> str: ...
    @overload
    def to_string(self, buf: FilePath | WriteBuffer[str], columns: Axes | None = ..., col_space: int | list[int] | dict[Hashable, int] | None = ..., header: bool | SequenceNotStr[str] = ..., index: bool = ..., na_rep: str = ..., formatters: fmt.FormattersType | None = ..., float_format: fmt.FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool = ..., decimal: str = ..., line_width: int | None = ..., min_rows: int | None = ..., max_colwidth: int | None = ..., encoding: str | None = ...) -> None: ...
    @property
    def style(self) -> Styler: ...
    def items(self) -> Iterable[tuple[Hashable, Series]]: ...
    def iterrows(self) -> Iterable[tuple[Hashable, Series]]: ...
    def itertuples(self, index: bool = True, name: str | None = 'Pandas') -> Iterable[tuple[Any, ...]]: ...
    def __len__(self) -> int: ...
    @overload
    def dot(self, other: Series) -> Series: ...
    @overload
    def dot(self, other: DataFrame | Index | ArrayLike) -> DataFrame: ...
    @overload
    def __matmul__(self, other: Series) -> Series: ...
    @overload
    def __matmul__(self, other: AnyArrayLike | DataFrame) -> DataFrame | Series: ...
    def __rmatmul__(self, other) -> DataFrame: ...
    @classmethod
    def from_dict(cls, data: dict, orient: FromDictOrient = 'columns', dtype: Dtype | None = None, columns: Axes | None = None) -> DataFrame: ...
    def to_numpy(self, dtype: npt.DTypeLike | None = None, copy: bool = False, na_value: object = ...) -> np.ndarray: ...
    @overload
    def to_dict(self, orient: Literal['dict', 'list', 'series', 'split', 'tight', 'index'] = ..., *, into: type[MutableMappingT] | MutableMappingT, index: bool = ...) -> MutableMappingT: ...
    @overload
    def to_dict(self, orient: Literal['records'], *, into: type[MutableMappingT] | MutableMappingT, index: bool = ...) -> list[MutableMappingT]: ...
    @overload
    def to_dict(self, orient: Literal['dict', 'list', 'series', 'split', 'tight', 'index'] = ..., *, into: type[dict] = ..., index: bool = ...) -> dict: ...
    @overload
    def to_dict(self, orient: Literal['records'], *, into: type[dict] = ..., index: bool = ...) -> list[dict]: ...
    def to_gbq(self, destination_table: str, project_id: str | None = None, chunksize: int | None = None, reauth: bool = False, if_exists: ToGbqIfexist = 'fail', auth_local_webserver: bool = True, table_schema: list[dict[str, str]] | None = None, location: str | None = None, progress_bar: bool = True, credentials: Incomplete | None = None) -> None: ...
    @classmethod
    def from_records(cls, data, index: Incomplete | None = None, exclude: Incomplete | None = None, columns: Incomplete | None = None, coerce_float: bool = False, nrows: int | None = None) -> DataFrame: ...
    def to_records(self, index: bool = True, column_dtypes: Incomplete | None = None, index_dtypes: Incomplete | None = None) -> np.rec.recarray: ...
    def to_stata(self, path: FilePath | WriteBuffer[bytes], *, convert_dates: dict[Hashable, str] | None = None, write_index: bool = True, byteorder: ToStataByteorder | None = None, time_stamp: datetime.datetime | None = None, data_label: str | None = None, variable_labels: dict[Hashable, str] | None = None, version: int | None = 114, convert_strl: Sequence[Hashable] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None, value_labels: dict[Hashable, dict[float, str]] | None = None) -> None: ...
    def to_feather(self, path: FilePath | WriteBuffer[bytes], **kwargs) -> None: ...
    def to_markdown(self, buf: FilePath | WriteBuffer[str] | None = None, mode: str = 'wt', index: bool = True, storage_options: StorageOptions | None = None, **kwargs) -> str | None: ...
    @overload
    def to_parquet(self, path: None = ..., engine: Literal['auto', 'pyarrow', 'fastparquet'] = ..., compression: str | None = ..., index: bool | None = ..., partition_cols: list[str] | None = ..., storage_options: StorageOptions = ..., **kwargs) -> bytes: ...
    @overload
    def to_parquet(self, path: FilePath | WriteBuffer[bytes], engine: Literal['auto', 'pyarrow', 'fastparquet'] = ..., compression: str | None = ..., index: bool | None = ..., partition_cols: list[str] | None = ..., storage_options: StorageOptions = ..., **kwargs) -> None: ...
    def to_orc(self, path: FilePath | WriteBuffer[bytes] | None = None, *, engine: Literal['pyarrow'] = 'pyarrow', index: bool | None = None, engine_kwargs: dict[str, Any] | None = None) -> bytes | None: ...
    @overload
    def to_html(self, buf: FilePath | WriteBuffer[str], columns: Axes | None = ..., col_space: ColspaceArgType | None = ..., header: bool = ..., index: bool = ..., na_rep: str = ..., formatters: FormattersType | None = ..., float_format: FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool | str = ..., decimal: str = ..., bold_rows: bool = ..., classes: str | list | tuple | None = ..., escape: bool = ..., notebook: bool = ..., border: int | bool | None = ..., table_id: str | None = ..., render_links: bool = ..., encoding: str | None = ...) -> None: ...
    @overload
    def to_html(self, buf: None = ..., columns: Axes | None = ..., col_space: ColspaceArgType | None = ..., header: bool = ..., index: bool = ..., na_rep: str = ..., formatters: FormattersType | None = ..., float_format: FloatFormatType | None = ..., sparsify: bool | None = ..., index_names: bool = ..., justify: str | None = ..., max_rows: int | None = ..., max_cols: int | None = ..., show_dimensions: bool | str = ..., decimal: str = ..., bold_rows: bool = ..., classes: str | list | tuple | None = ..., escape: bool = ..., notebook: bool = ..., border: int | bool | None = ..., table_id: str | None = ..., render_links: bool = ..., encoding: str | None = ...) -> str: ...
    @overload
    def to_xml(self, path_or_buffer: None = ..., *, index: bool = ..., root_name: str | None = ..., row_name: str | None = ..., na_rep: str | None = ..., attr_cols: list[str] | None = ..., elem_cols: list[str] | None = ..., namespaces: dict[str | None, str] | None = ..., prefix: str | None = ..., encoding: str = ..., xml_declaration: bool | None = ..., pretty_print: bool | None = ..., parser: XMLParsers | None = ..., stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = ..., compression: CompressionOptions = ..., storage_options: StorageOptions | None = ...) -> str: ...
    @overload
    def to_xml(self, path_or_buffer: FilePath | WriteBuffer[bytes] | WriteBuffer[str], *, index: bool = ..., root_name: str | None = ..., row_name: str | None = ..., na_rep: str | None = ..., attr_cols: list[str] | None = ..., elem_cols: list[str] | None = ..., namespaces: dict[str | None, str] | None = ..., prefix: str | None = ..., encoding: str = ..., xml_declaration: bool | None = ..., pretty_print: bool | None = ..., parser: XMLParsers | None = ..., stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = ..., compression: CompressionOptions = ..., storage_options: StorageOptions | None = ...) -> None: ...
    def info(self, verbose: bool | None = None, buf: WriteBuffer[str] | None = None, max_cols: int | None = None, memory_usage: bool | str | None = None, show_counts: bool | None = None) -> None: ...
    def memory_usage(self, index: bool = True, deep: bool = False) -> Series: ...
    def transpose(self, *args, copy: bool = False) -> DataFrame: ...
    @property
    def T(self) -> DataFrame: ...
    def __getitem__(self, key): ...
    def isetitem(self, loc, value) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    @overload
    def query(self, expr: str, *, inplace: Literal[False] = ..., **kwargs) -> DataFrame: ...
    @overload
    def query(self, expr: str, *, inplace: Literal[True], **kwargs) -> None: ...
    @overload
    def query(self, expr: str, *, inplace: bool = ..., **kwargs) -> DataFrame | None: ...
    @overload
    def eval(self, expr: str, *, inplace: Literal[False] = ..., **kwargs) -> Any: ...
    @overload
    def eval(self, expr: str, *, inplace: Literal[True], **kwargs) -> None: ...
    def select_dtypes(self, include: Incomplete | None = None, exclude: Incomplete | None = None) -> Self: ...
    def insert(self, loc: int, column: Hashable, value: Scalar | AnyArrayLike, allow_duplicates: bool | lib.NoDefault = ...) -> None: ...
    def assign(self, **kwargs) -> DataFrame: ...
    def set_axis(self, labels, *, axis: Axis = 0, copy: bool | None = None) -> DataFrame: ...
    def reindex(self, labels: Incomplete | None = None, *, index: Incomplete | None = None, columns: Incomplete | None = None, axis: Axis | None = None, method: ReindexMethod | None = None, copy: bool | None = None, level: Level | None = None, fill_value: Scalar | None = ..., limit: int | None = None, tolerance: Incomplete | None = None) -> DataFrame: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Level = ..., inplace: Literal[True], errors: IgnoreRaise = ...) -> None: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Level = ..., inplace: Literal[False] = ..., errors: IgnoreRaise = ...) -> DataFrame: ...
    @overload
    def drop(self, labels: IndexLabel = ..., *, axis: Axis = ..., index: IndexLabel = ..., columns: IndexLabel = ..., level: Level = ..., inplace: bool = ..., errors: IgnoreRaise = ...) -> DataFrame | None: ...
    @overload
    def rename(self, mapper: Renamer | None = ..., *, index: Renamer | None = ..., columns: Renamer | None = ..., axis: Axis | None = ..., copy: bool | None = ..., inplace: Literal[True], level: Level = ..., errors: IgnoreRaise = ...) -> None: ...
    @overload
    def rename(self, mapper: Renamer | None = ..., *, index: Renamer | None = ..., columns: Renamer | None = ..., axis: Axis | None = ..., copy: bool | None = ..., inplace: Literal[False] = ..., level: Level = ..., errors: IgnoreRaise = ...) -> DataFrame: ...
    @overload
    def rename(self, mapper: Renamer | None = ..., *, index: Renamer | None = ..., columns: Renamer | None = ..., axis: Axis | None = ..., copy: bool | None = ..., inplace: bool = ..., level: Level = ..., errors: IgnoreRaise = ...) -> DataFrame | None: ...
    def pop(self, item: Hashable) -> Series: ...
    def shift(self, periods: int | Sequence[int] = 1, freq: Frequency | None = None, axis: Axis = 0, fill_value: Hashable = ..., suffix: str | None = None) -> DataFrame: ...
    @overload
    def set_index(self, keys, *, drop: bool = ..., append: bool = ..., inplace: Literal[False] = ..., verify_integrity: bool = ...) -> DataFrame: ...
    @overload
    def set_index(self, keys, *, drop: bool = ..., append: bool = ..., inplace: Literal[True], verify_integrity: bool = ...) -> None: ...
    @overload
    def reset_index(self, level: IndexLabel = ..., *, drop: bool = ..., inplace: Literal[False] = ..., col_level: Hashable = ..., col_fill: Hashable = ..., allow_duplicates: bool | lib.NoDefault = ..., names: Hashable | Sequence[Hashable] | None = None) -> DataFrame: ...
    @overload
    def reset_index(self, level: IndexLabel = ..., *, drop: bool = ..., inplace: Literal[True], col_level: Hashable = ..., col_fill: Hashable = ..., allow_duplicates: bool | lib.NoDefault = ..., names: Hashable | Sequence[Hashable] | None = None) -> None: ...
    @overload
    def reset_index(self, level: IndexLabel = ..., *, drop: bool = ..., inplace: bool = ..., col_level: Hashable = ..., col_fill: Hashable = ..., allow_duplicates: bool | lib.NoDefault = ..., names: Hashable | Sequence[Hashable] | None = None) -> DataFrame | None: ...
    def isna(self) -> DataFrame: ...
    def isnull(self) -> DataFrame: ...
    def notna(self) -> DataFrame: ...
    def notnull(self) -> DataFrame: ...
    @overload
    def dropna(self, *, axis: Axis = ..., how: AnyAll | lib.NoDefault = ..., thresh: int | lib.NoDefault = ..., subset: IndexLabel = ..., inplace: Literal[False] = ..., ignore_index: bool = ...) -> DataFrame: ...
    @overload
    def dropna(self, *, axis: Axis = ..., how: AnyAll | lib.NoDefault = ..., thresh: int | lib.NoDefault = ..., subset: IndexLabel = ..., inplace: Literal[True], ignore_index: bool = ...) -> None: ...
    @overload
    def drop_duplicates(self, subset: Hashable | Sequence[Hashable] | None = ..., *, keep: DropKeep = ..., inplace: Literal[True], ignore_index: bool = ...) -> None: ...
    @overload
    def drop_duplicates(self, subset: Hashable | Sequence[Hashable] | None = ..., *, keep: DropKeep = ..., inplace: Literal[False] = ..., ignore_index: bool = ...) -> DataFrame: ...
    @overload
    def drop_duplicates(self, subset: Hashable | Sequence[Hashable] | None = ..., *, keep: DropKeep = ..., inplace: bool = ..., ignore_index: bool = ...) -> DataFrame | None: ...
    def duplicated(self, subset: Hashable | Sequence[Hashable] | None = None, keep: DropKeep = 'first') -> Series: ...
    @overload
    def sort_values(self, by: IndexLabel, *, axis: Axis = ..., ascending=..., inplace: Literal[False] = ..., kind: SortKind = ..., na_position: NaPosition = ..., ignore_index: bool = ..., key: ValueKeyFunc = ...) -> DataFrame: ...
    @overload
    def sort_values(self, by: IndexLabel, *, axis: Axis = ..., ascending=..., inplace: Literal[True], kind: SortKind = ..., na_position: str = ..., ignore_index: bool = ..., key: ValueKeyFunc = ...) -> None: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: bool | Sequence[bool] = ..., inplace: Literal[True], kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ...) -> None: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: bool | Sequence[bool] = ..., inplace: Literal[False] = ..., kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ...) -> DataFrame: ...
    @overload
    def sort_index(self, *, axis: Axis = ..., level: IndexLabel = ..., ascending: bool | Sequence[bool] = ..., inplace: bool = ..., kind: SortKind = ..., na_position: NaPosition = ..., sort_remaining: bool = ..., ignore_index: bool = ..., key: IndexKeyFunc = ...) -> DataFrame | None: ...
    def value_counts(self, subset: IndexLabel | None = None, normalize: bool = False, sort: bool = True, ascending: bool = False, dropna: bool = True) -> Series: ...
    def nlargest(self, n: int, columns: IndexLabel, keep: NsmallestNlargestKeep = 'first') -> DataFrame: ...
    def nsmallest(self, n: int, columns: IndexLabel, keep: NsmallestNlargestKeep = 'first') -> DataFrame: ...
    def swaplevel(self, i: Axis = -2, j: Axis = -1, axis: Axis = 0) -> DataFrame: ...
    def reorder_levels(self, order: Sequence[int | str], axis: Axis = 0) -> DataFrame: ...
    def __divmod__(self, other) -> tuple[DataFrame, DataFrame]: ...
    def __rdivmod__(self, other) -> tuple[DataFrame, DataFrame]: ...
    def eq(self, other, axis: Axis = 'columns', level: Incomplete | None = None) -> DataFrame: ...
    def ne(self, other, axis: Axis = 'columns', level: Incomplete | None = None) -> DataFrame: ...
    def le(self, other, axis: Axis = 'columns', level: Incomplete | None = None) -> DataFrame: ...
    def lt(self, other, axis: Axis = 'columns', level: Incomplete | None = None) -> DataFrame: ...
    def ge(self, other, axis: Axis = 'columns', level: Incomplete | None = None) -> DataFrame: ...
    def gt(self, other, axis: Axis = 'columns', level: Incomplete | None = None) -> DataFrame: ...
    def add(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def radd(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def sub(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    subtract = sub
    def rsub(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def mul(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    multiply = mul
    def rmul(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def truediv(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    div = truediv
    divide = truediv
    def rtruediv(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    rdiv = rtruediv
    def floordiv(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def rfloordiv(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def mod(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def rmod(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def pow(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def rpow(self, other, axis: Axis = 'columns', level: Incomplete | None = None, fill_value: Incomplete | None = None) -> DataFrame: ...
    def compare(self, other: DataFrame, align_axis: Axis = 1, keep_shape: bool = False, keep_equal: bool = False, result_names: Suffixes = ('self', 'other')) -> DataFrame: ...
    def combine(self, other: DataFrame, func: Callable[[Series, Series], Series | Hashable], fill_value: Incomplete | None = None, overwrite: bool = True) -> DataFrame: ...
    def combine_first(self, other: DataFrame) -> DataFrame: ...
    def update(self, other, join: UpdateJoin = 'left', overwrite: bool = True, filter_func: Incomplete | None = None, errors: IgnoreRaise = 'ignore') -> None: ...
    def groupby(self, by: Incomplete | None = None, axis: Axis | lib.NoDefault = ..., level: IndexLabel | None = None, as_index: bool = True, sort: bool = True, group_keys: bool = True, observed: bool | lib.NoDefault = ..., dropna: bool = True) -> DataFrameGroupBy: ...
    def pivot(self, *, columns, index=..., values=...) -> DataFrame: ...
    def pivot_table(self, values: Incomplete | None = None, index: Incomplete | None = None, columns: Incomplete | None = None, aggfunc: AggFuncType = 'mean', fill_value: Incomplete | None = None, margins: bool = False, dropna: bool = True, margins_name: Level = 'All', observed: bool | lib.NoDefault = ..., sort: bool = True) -> DataFrame: ...
    def stack(self, level: IndexLabel = -1, dropna: bool | lib.NoDefault = ..., sort: bool | lib.NoDefault = ..., future_stack: bool = False): ...
    def explode(self, column: IndexLabel, ignore_index: bool = False) -> DataFrame: ...
    def unstack(self, level: IndexLabel = -1, fill_value: Incomplete | None = None, sort: bool = True): ...
    def melt(self, id_vars: Incomplete | None = None, value_vars: Incomplete | None = None, var_name: Incomplete | None = None, value_name: Hashable = 'value', col_level: Level | None = None, ignore_index: bool = True) -> DataFrame: ...
    def diff(self, periods: int = 1, axis: Axis = 0) -> DataFrame: ...
    def aggregate(self, func: Incomplete | None = None, axis: Axis = 0, *args, **kwargs): ...
    agg = aggregate
    def transform(self, func: AggFuncType, axis: Axis = 0, *args, **kwargs) -> DataFrame: ...
    def apply(self, func: AggFuncType, axis: Axis = 0, raw: bool = False, result_type: Literal['expand', 'reduce', 'broadcast'] | None = None, args=(), by_row: Literal[False, 'compat'] = 'compat', engine: Literal['python', 'numba'] = 'python', engine_kwargs: dict[str, bool] | None = None, **kwargs): ...
    def map(self, func: PythonFuncType, na_action: str | None = None, **kwargs) -> DataFrame: ...
    def applymap(self, func: PythonFuncType, na_action: NaAction | None = None, **kwargs) -> DataFrame: ...
    def join(self, other: DataFrame | Series | Iterable[DataFrame | Series], on: IndexLabel | None = None, how: MergeHow = 'left', lsuffix: str = '', rsuffix: str = '', sort: bool = False, validate: JoinValidate | None = None) -> DataFrame: ...
    def merge(self, right: DataFrame | Series, how: MergeHow = 'inner', on: IndexLabel | AnyArrayLike | None = None, left_on: IndexLabel | AnyArrayLike | None = None, right_on: IndexLabel | AnyArrayLike | None = None, left_index: bool = False, right_index: bool = False, sort: bool = False, suffixes: Suffixes = ('_x', '_y'), copy: bool | None = None, indicator: str | bool = False, validate: MergeValidate | None = None) -> DataFrame: ...
    def round(self, decimals: int | dict[IndexLabel, int] | Series = 0, *args, **kwargs) -> DataFrame: ...
    def corr(self, method: CorrelationMethod = 'pearson', min_periods: int = 1, numeric_only: bool = False) -> DataFrame: ...
    def cov(self, min_periods: int | None = None, ddof: int | None = 1, numeric_only: bool = False) -> DataFrame: ...
    def corrwith(self, other: DataFrame | Series, axis: Axis = 0, drop: bool = False, method: CorrelationMethod = 'pearson', numeric_only: bool = False) -> Series: ...
    def count(self, axis: Axis = 0, numeric_only: bool = False): ...
    def any(self, *, axis: Axis | None = 0, bool_only: bool = False, skipna: bool = True, **kwargs) -> Series | bool: ...
    def all(self, axis: Axis | None = 0, bool_only: bool = False, skipna: bool = True, **kwargs) -> Series | bool: ...
    def min(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, **kwargs): ...
    def max(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, **kwargs): ...
    def sum(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, min_count: int = 0, **kwargs): ...
    def prod(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, min_count: int = 0, **kwargs): ...
    def mean(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, **kwargs): ...
    def median(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, **kwargs): ...
    def sem(self, axis: Axis | None = 0, skipna: bool = True, ddof: int = 1, numeric_only: bool = False, **kwargs): ...
    def var(self, axis: Axis | None = 0, skipna: bool = True, ddof: int = 1, numeric_only: bool = False, **kwargs): ...
    def std(self, axis: Axis | None = 0, skipna: bool = True, ddof: int = 1, numeric_only: bool = False, **kwargs): ...
    def skew(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, **kwargs): ...
    def kurt(self, axis: Axis | None = 0, skipna: bool = True, numeric_only: bool = False, **kwargs): ...
    kurtosis = kurt
    product = prod
    def cummin(self, axis: Axis | None = None, skipna: bool = True, *args, **kwargs): ...
    def cummax(self, axis: Axis | None = None, skipna: bool = True, *args, **kwargs): ...
    def cumsum(self, axis: Axis | None = None, skipna: bool = True, *args, **kwargs): ...
    def cumprod(self, axis: Axis | None = None, skipna: bool = True, *args, **kwargs): ...
    def nunique(self, axis: Axis = 0, dropna: bool = True) -> Series: ...
    def idxmin(self, axis: Axis = 0, skipna: bool = True, numeric_only: bool = False) -> Series: ...
    def idxmax(self, axis: Axis = 0, skipna: bool = True, numeric_only: bool = False) -> Series: ...
    def mode(self, axis: Axis = 0, numeric_only: bool = False, dropna: bool = True) -> DataFrame: ...
    @overload
    def quantile(self, q: float = ..., axis: Axis = ..., numeric_only: bool = ..., interpolation: QuantileInterpolation = ..., method: Literal['single', 'table'] = ...) -> Series: ...
    @overload
    def quantile(self, q: AnyArrayLike | Sequence[float], axis: Axis = ..., numeric_only: bool = ..., interpolation: QuantileInterpolation = ..., method: Literal['single', 'table'] = ...) -> Series | DataFrame: ...
    @overload
    def quantile(self, q: float | AnyArrayLike | Sequence[float] = ..., axis: Axis = ..., numeric_only: bool = ..., interpolation: QuantileInterpolation = ..., method: Literal['single', 'table'] = ...) -> Series | DataFrame: ...
    def to_timestamp(self, freq: Frequency | None = None, how: ToTimestampHow = 'start', axis: Axis = 0, copy: bool | None = None) -> DataFrame: ...
    def to_period(self, freq: Frequency | None = None, axis: Axis = 0, copy: bool | None = None) -> DataFrame: ...
    def isin(self, values: Series | DataFrame | Sequence | Mapping) -> DataFrame: ...
    index: Incomplete
    columns: Incomplete
    plot: Incomplete
    hist: Incomplete
    boxplot: Incomplete
    sparse: Incomplete
    @property
    def values(self) -> np.ndarray: ...
