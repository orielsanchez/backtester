import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Mapping
from pandas import ArrowDtype as ArrowDtype, DataFrame as DataFrame, Index as Index, MultiIndex as MultiIndex, Series as Series, isna as isna, notna as notna, to_datetime as to_datetime
from pandas._libs import lib as lib
from pandas._libs.json import ujson_dumps as ujson_dumps, ujson_loads as ujson_loads
from pandas._libs.tslibs import iNaT as iNaT
from pandas._typing import CompressionOptions as CompressionOptions, DtypeArg as DtypeArg, DtypeBackend as DtypeBackend, FilePath as FilePath, IndexLabel as IndexLabel, JSONEngine as JSONEngine, JSONSerializable as JSONSerializable, ReadBuffer as ReadBuffer, Self as Self, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import ensure_str as ensure_str, is_string_dtype as is_string_dtype
from pandas.core.dtypes.dtypes import PeriodDtype as PeriodDtype
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.reshape.concat import concat as concat
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import IOHandles as IOHandles, dedup_names as dedup_names, extension_to_compression as extension_to_compression, file_exists as file_exists, get_handle as get_handle, is_fsspec_url as is_fsspec_url, is_potential_multi_index as is_potential_multi_index, is_url as is_url, stringify_path as stringify_path
from pandas.io.json._normalize import convert_to_line_delimits as convert_to_line_delimits
from pandas.io.json._table_schema import build_table_schema as build_table_schema, parse_table_schema as parse_table_schema
from pandas.io.parsers.readers import validate_integer as validate_integer
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from types import TracebackType
from typing import Any, Callable, Generic, Literal, TypeVar, overload

FrameSeriesStrT = TypeVar('FrameSeriesStrT', bound=Literal['frame', 'series'])

@overload
def to_json(path_or_buf: FilePath | WriteBuffer[str] | WriteBuffer[bytes], obj: NDFrame, orient: str | None = ..., date_format: str = ..., double_precision: int = ..., force_ascii: bool = ..., date_unit: str = ..., default_handler: Callable[[Any], JSONSerializable] | None = ..., lines: bool = ..., compression: CompressionOptions = ..., index: bool | None = ..., indent: int = ..., storage_options: StorageOptions = ..., mode: Literal['a', 'w'] = ...) -> None: ...
@overload
def to_json(path_or_buf: None, obj: NDFrame, orient: str | None = ..., date_format: str = ..., double_precision: int = ..., force_ascii: bool = ..., date_unit: str = ..., default_handler: Callable[[Any], JSONSerializable] | None = ..., lines: bool = ..., compression: CompressionOptions = ..., index: bool | None = ..., indent: int = ..., storage_options: StorageOptions = ..., mode: Literal['a', 'w'] = ...) -> str: ...

class Writer(ABC, metaclass=abc.ABCMeta):
    obj: Incomplete
    orient: Incomplete
    date_format: Incomplete
    double_precision: Incomplete
    ensure_ascii: Incomplete
    date_unit: Incomplete
    default_handler: Incomplete
    index: Incomplete
    indent: Incomplete
    is_copy: Incomplete
    def __init__(self, obj: NDFrame, orient: str | None, date_format: str, double_precision: int, ensure_ascii: bool, date_unit: str, index: bool, default_handler: Callable[[Any], JSONSerializable] | None = None, indent: int = 0) -> None: ...
    def write(self) -> str: ...
    @property
    @abstractmethod
    def obj_to_write(self) -> NDFrame | Mapping[IndexLabel, Any]: ...

class SeriesWriter(Writer):
    @property
    def obj_to_write(self) -> NDFrame | Mapping[IndexLabel, Any]: ...

class FrameWriter(Writer):
    @property
    def obj_to_write(self) -> NDFrame | Mapping[IndexLabel, Any]: ...

class JSONTableWriter(FrameWriter):
    schema: Incomplete
    obj: Incomplete
    date_format: str
    orient: str
    index: Incomplete
    def __init__(self, obj, orient: str | None, date_format: str, double_precision: int, ensure_ascii: bool, date_unit: str, index: bool, default_handler: Callable[[Any], JSONSerializable] | None = None, indent: int = 0) -> None: ...
    @property
    def obj_to_write(self) -> NDFrame | Mapping[IndexLabel, Any]: ...

@overload
def read_json(path_or_buf: FilePath | ReadBuffer[str] | ReadBuffer[bytes], *, orient: str | None = ..., typ: Literal['frame'] = ..., dtype: DtypeArg | None = ..., convert_axes: bool | None = ..., convert_dates: bool | list[str] = ..., keep_default_dates: bool = ..., precise_float: bool = ..., date_unit: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., lines: bool = ..., chunksize: int, compression: CompressionOptions = ..., nrows: int | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ..., engine: JSONEngine = ...) -> JsonReader[Literal['frame']]: ...
@overload
def read_json(path_or_buf: FilePath | ReadBuffer[str] | ReadBuffer[bytes], *, orient: str | None = ..., typ: Literal['series'], dtype: DtypeArg | None = ..., convert_axes: bool | None = ..., convert_dates: bool | list[str] = ..., keep_default_dates: bool = ..., precise_float: bool = ..., date_unit: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., lines: bool = ..., chunksize: int, compression: CompressionOptions = ..., nrows: int | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ..., engine: JSONEngine = ...) -> JsonReader[Literal['series']]: ...
@overload
def read_json(path_or_buf: FilePath | ReadBuffer[str] | ReadBuffer[bytes], *, orient: str | None = ..., typ: Literal['series'], dtype: DtypeArg | None = ..., convert_axes: bool | None = ..., convert_dates: bool | list[str] = ..., keep_default_dates: bool = ..., precise_float: bool = ..., date_unit: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., lines: bool = ..., chunksize: None = ..., compression: CompressionOptions = ..., nrows: int | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ..., engine: JSONEngine = ...) -> Series: ...
@overload
def read_json(path_or_buf: FilePath | ReadBuffer[str] | ReadBuffer[bytes], *, orient: str | None = ..., typ: Literal['frame'] = ..., dtype: DtypeArg | None = ..., convert_axes: bool | None = ..., convert_dates: bool | list[str] = ..., keep_default_dates: bool = ..., precise_float: bool = ..., date_unit: str | None = ..., encoding: str | None = ..., encoding_errors: str | None = ..., lines: bool = ..., chunksize: None = ..., compression: CompressionOptions = ..., nrows: int | None = ..., storage_options: StorageOptions = ..., dtype_backend: DtypeBackend | lib.NoDefault = ..., engine: JSONEngine = ...) -> DataFrame: ...

class JsonReader(abc.Iterator, Generic[FrameSeriesStrT]):
    orient: Incomplete
    typ: Incomplete
    dtype: Incomplete
    convert_axes: Incomplete
    convert_dates: Incomplete
    keep_default_dates: Incomplete
    precise_float: Incomplete
    date_unit: Incomplete
    encoding: Incomplete
    engine: Incomplete
    compression: Incomplete
    storage_options: Incomplete
    lines: Incomplete
    chunksize: Incomplete
    nrows_seen: int
    nrows: Incomplete
    encoding_errors: Incomplete
    handles: IOHandles[str] | None
    dtype_backend: Incomplete
    data: Incomplete
    def __init__(self, filepath_or_buffer, orient, typ: FrameSeriesStrT, dtype, convert_axes: bool | None, convert_dates, keep_default_dates: bool, precise_float: bool, date_unit, encoding, lines: bool, chunksize: int | None, compression: CompressionOptions, nrows: int | None, storage_options: StorageOptions | None = None, encoding_errors: str | None = 'strict', dtype_backend: DtypeBackend | lib.NoDefault = ..., engine: JSONEngine = 'ujson') -> None: ...
    @overload
    def read(self) -> DataFrame: ...
    @overload
    def read(self) -> Series: ...
    @overload
    def read(self) -> DataFrame | Series: ...
    def close(self) -> None: ...
    def __iter__(self) -> Self: ...
    @overload
    def __next__(self) -> DataFrame: ...
    @overload
    def __next__(self) -> Series: ...
    @overload
    def __next__(self) -> DataFrame | Series: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

class Parser:
    json: str
    orient: Incomplete
    dtype: Incomplete
    min_stamp: Incomplete
    precise_float: Incomplete
    convert_axes: Incomplete
    convert_dates: Incomplete
    date_unit: Incomplete
    keep_default_dates: Incomplete
    obj: DataFrame | Series | None
    dtype_backend: Incomplete
    def __init__(self, json: str, orient, dtype: DtypeArg | None = None, convert_axes: bool = True, convert_dates: bool | list[str] = True, keep_default_dates: bool = False, precise_float: bool = False, date_unit: Incomplete | None = None, dtype_backend: DtypeBackend | lib.NoDefault = ...) -> None: ...
    def check_keys_split(self, decoded: dict) -> None: ...
    def parse(self): ...

class SeriesParser(Parser):
    obj: Series | None

class FrameParser(Parser):
    obj: DataFrame | None
