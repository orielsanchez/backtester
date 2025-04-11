import numpy as np
from _typeshed import Incomplete
from collections import abc
from collections.abc import Hashable, Sequence
from datetime import datetime
from pandas import Categorical as Categorical, DatetimeIndex as DatetimeIndex, NaT as NaT, Timestamp as Timestamp, isna as isna, to_datetime as to_datetime, to_timedelta as to_timedelta
from pandas._libs import lib as lib
from pandas._libs.lib import infer_dtype as infer_dtype
from pandas._libs.writers import max_len_string_array as max_len_string_array
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer, Self as Self, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.dtypes.base import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.common import ensure_object as ensure_object, is_numeric_dtype as is_numeric_dtype, is_string_dtype as is_string_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.base import Index as Index
from pandas.core.indexes.range import RangeIndex as RangeIndex
from pandas.core.series import Series as Series
from pandas.errors import CategoricalConversionWarning as CategoricalConversionWarning, InvalidColumnName as InvalidColumnName, PossiblePrecisionLoss as PossiblePrecisionLoss, ValueLabelTypeMismatch as ValueLabelTypeMismatch
from pandas.io.common import get_handle as get_handle
from pandas.util._decorators import Appender as Appender, doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from types import TracebackType
from typing import Final, Literal

stata_epoch: Final[Incomplete]
excessive_string_length_error: Final[str]
precision_loss_doc: Final[str]
value_label_mismatch_doc: Final[str]
invalid_name_doc: Final[str]
categorical_conversion_warning: Final[str]

class StataValueLabel:
    labname: Incomplete
    value_labels: Incomplete
    def __init__(self, catarray: Series, encoding: Literal['latin-1', 'utf-8'] = 'latin-1') -> None: ...
    def generate_value_label(self, byteorder: str) -> bytes: ...

class StataNonCatValueLabel(StataValueLabel):
    labname: Incomplete
    value_labels: Incomplete
    def __init__(self, labname: str, value_labels: dict[float, str], encoding: Literal['latin-1', 'utf-8'] = 'latin-1') -> None: ...

class StataMissingValue:
    MISSING_VALUES: dict[float, str]
    bases: Final[Incomplete]
    float32_base: bytes
    increment_32: int
    key: Incomplete
    int_value: Incomplete
    float64_base: bytes
    increment_64: Incomplete
    BASE_MISSING_VALUES: Final[Incomplete]
    def __init__(self, value: float) -> None: ...
    @property
    def string(self) -> str: ...
    @property
    def value(self) -> float: ...
    def __eq__(self, other: object) -> bool: ...
    @classmethod
    def get_base_missing_value(cls, dtype: np.dtype) -> float: ...

class StataParser:
    DTYPE_MAP: Incomplete
    DTYPE_MAP_XML: dict[int, np.dtype]
    TYPE_MAP: Incomplete
    TYPE_MAP_XML: Incomplete
    VALID_RANGE: Incomplete
    OLD_TYPE_MAPPING: Incomplete
    MISSING_VALUES: Incomplete
    NUMPY_TYPE_MAP: Incomplete
    RESERVED_WORDS: Incomplete
    def __init__(self) -> None: ...

class StataReader(StataParser, abc.Iterator):
    __doc__: Incomplete
    def __init__(self, path_or_buf: FilePath | ReadBuffer[bytes], convert_dates: bool = True, convert_categoricals: bool = True, index_col: str | None = None, convert_missing: bool = False, preserve_dtypes: bool = True, columns: Sequence[str] | None = None, order_categoricals: bool = True, chunksize: int | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def close(self) -> None: ...
    def __next__(self) -> DataFrame: ...
    def get_chunk(self, size: int | None = None) -> DataFrame: ...
    def read(self, nrows: int | None = None, convert_dates: bool | None = None, convert_categoricals: bool | None = None, index_col: str | None = None, convert_missing: bool | None = None, preserve_dtypes: bool | None = None, columns: Sequence[str] | None = None, order_categoricals: bool | None = None) -> DataFrame: ...
    @property
    def data_label(self) -> str: ...
    @property
    def time_stamp(self) -> str: ...
    def variable_labels(self) -> dict[str, str]: ...
    def value_labels(self) -> dict[str, dict[float, str]]: ...

def read_stata(filepath_or_buffer: FilePath | ReadBuffer[bytes], *, convert_dates: bool = True, convert_categoricals: bool = True, index_col: str | None = None, convert_missing: bool = False, preserve_dtypes: bool = True, columns: Sequence[str] | None = None, order_categoricals: bool = True, chunksize: int | None = None, iterator: bool = False, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None) -> DataFrame | StataReader: ...

class StataWriter(StataParser):
    data: Incomplete
    storage_options: Incomplete
    type_converters: Incomplete
    def __init__(self, fname: FilePath | WriteBuffer[bytes], data: DataFrame, convert_dates: dict[Hashable, str] | None = None, write_index: bool = True, byteorder: str | None = None, time_stamp: datetime | None = None, data_label: str | None = None, variable_labels: dict[Hashable, str] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None, *, value_labels: dict[Hashable, dict[float, str]] | None = None) -> None: ...
    def write_file(self) -> None: ...

class StataStrLWriter:
    df: Incomplete
    columns: Incomplete
    def __init__(self, df: DataFrame, columns: Sequence[str], version: int = 117, byteorder: str | None = None) -> None: ...
    def generate_table(self) -> tuple[dict[str, tuple[int, int]], DataFrame]: ...
    def generate_blob(self, gso_table: dict[str, tuple[int, int]]) -> bytes: ...

class StataWriter117(StataWriter):
    def __init__(self, fname: FilePath | WriteBuffer[bytes], data: DataFrame, convert_dates: dict[Hashable, str] | None = None, write_index: bool = True, byteorder: str | None = None, time_stamp: datetime | None = None, data_label: str | None = None, variable_labels: dict[Hashable, str] | None = None, convert_strl: Sequence[Hashable] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None, *, value_labels: dict[Hashable, dict[float, str]] | None = None) -> None: ...

class StataWriterUTF8(StataWriter117):
    def __init__(self, fname: FilePath | WriteBuffer[bytes], data: DataFrame, convert_dates: dict[Hashable, str] | None = None, write_index: bool = True, byteorder: str | None = None, time_stamp: datetime | None = None, data_label: str | None = None, variable_labels: dict[Hashable, str] | None = None, convert_strl: Sequence[Hashable] | None = None, version: int | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None, *, value_labels: dict[Hashable, dict[float, str]] | None = None) -> None: ...
