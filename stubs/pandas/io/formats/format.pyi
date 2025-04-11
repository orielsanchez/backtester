import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable, Sequence
from pandas import DataFrame as DataFrame, Series as Series
from pandas._config.config import get_option as get_option, set_option as set_option
from pandas._libs import lib as lib
from pandas._libs.missing import NA as NA
from pandas._libs.tslibs import NaT as NaT, Timedelta as Timedelta, Timestamp as Timestamp
from pandas._libs.tslibs.nattype import NaTType as NaTType
from pandas._typing import ArrayLike as ArrayLike, Axes as Axes, ColspaceArgType as ColspaceArgType, ColspaceType as ColspaceType, CompressionOptions as CompressionOptions, FilePath as FilePath, FloatFormatType as FloatFormatType, FormattersType as FormattersType, IndexLabel as IndexLabel, SequenceNotStr as SequenceNotStr, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.arrays import Categorical as Categorical, DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, TimedeltaArray as TimedeltaArray
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.base import PandasObject as PandasObject
from pandas.core.dtypes.common import is_complex_dtype as is_complex_dtype, is_float as is_float, is_integer as is_integer, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, PeriodIndex as PeriodIndex, ensure_index as ensure_index
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex as TimedeltaIndex
from pandas.core.reshape.concat import concat as concat
from pandas.io.common import check_parent_directory as check_parent_directory, stringify_path as stringify_path
from pandas.io.formats import printing as printing
from typing import Any, Callable, Final

common_docstring: Final[str]
VALID_JUSTIFY_PARAMETERS: Incomplete
return_docstring: Final[str]

class SeriesFormatter:
    series: Incomplete
    buf: Incomplete
    name: Incomplete
    na_rep: Incomplete
    header: Incomplete
    length: Incomplete
    index: Incomplete
    max_rows: Incomplete
    min_rows: Incomplete
    float_format: Incomplete
    dtype: Incomplete
    adj: Incomplete
    def __init__(self, series: Series, *, length: bool | str = True, header: bool = True, index: bool = True, na_rep: str = 'NaN', name: bool = False, float_format: str | None = None, dtype: bool = True, max_rows: int | None = None, min_rows: int | None = None) -> None: ...
    def to_string(self) -> str: ...

def get_dataframe_repr_params() -> dict[str, Any]: ...
def get_series_repr_params() -> dict[str, Any]: ...

class DataFrameFormatter:
    __doc__: Incomplete
    frame: Incomplete
    columns: Incomplete
    col_space: Incomplete
    header: Incomplete
    index: Incomplete
    na_rep: Incomplete
    formatters: Incomplete
    justify: Incomplete
    float_format: Incomplete
    sparsify: Incomplete
    show_index_names: Incomplete
    decimal: Incomplete
    bold_rows: Incomplete
    escape: Incomplete
    max_rows: Incomplete
    min_rows: Incomplete
    max_cols: Incomplete
    show_dimensions: Incomplete
    max_cols_fitted: Incomplete
    max_rows_fitted: Incomplete
    tr_frame: Incomplete
    adj: Incomplete
    def __init__(self, frame: DataFrame, columns: Axes | None = None, col_space: ColspaceArgType | None = None, header: bool | SequenceNotStr[str] = True, index: bool = True, na_rep: str = 'NaN', formatters: FormattersType | None = None, justify: str | None = None, float_format: FloatFormatType | None = None, sparsify: bool | None = None, index_names: bool = True, max_rows: int | None = None, min_rows: int | None = None, max_cols: int | None = None, show_dimensions: bool | str = False, decimal: str = '.', bold_rows: bool = False, escape: bool = True) -> None: ...
    def get_strcols(self) -> list[list[str]]: ...
    @property
    def should_show_dimensions(self) -> bool: ...
    @property
    def is_truncated(self) -> bool: ...
    @property
    def is_truncated_horizontally(self) -> bool: ...
    @property
    def is_truncated_vertically(self) -> bool: ...
    @property
    def dimensions_info(self) -> str: ...
    @property
    def has_index_names(self) -> bool: ...
    @property
    def has_column_names(self) -> bool: ...
    @property
    def show_row_idx_names(self) -> bool: ...
    @property
    def show_col_idx_names(self) -> bool: ...
    @property
    def max_rows_displayed(self) -> int: ...
    def truncate(self) -> None: ...
    def format_col(self, i: int) -> list[str]: ...

class DataFrameRenderer:
    fmt: Incomplete
    def __init__(self, fmt: DataFrameFormatter) -> None: ...
    def to_html(self, buf: FilePath | WriteBuffer[str] | None = None, encoding: str | None = None, classes: str | list | tuple | None = None, notebook: bool = False, border: int | bool | None = None, table_id: str | None = None, render_links: bool = False) -> str | None: ...
    def to_string(self, buf: FilePath | WriteBuffer[str] | None = None, encoding: str | None = None, line_width: int | None = None) -> str | None: ...
    def to_csv(self, path_or_buf: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None, encoding: str | None = None, sep: str = ',', columns: Sequence[Hashable] | None = None, index_label: IndexLabel | None = None, mode: str = 'w', compression: CompressionOptions = 'infer', quoting: int | None = None, quotechar: str = '"', lineterminator: str | None = None, chunksize: int | None = None, date_format: str | None = None, doublequote: bool = True, escapechar: str | None = None, errors: str = 'strict', storage_options: StorageOptions | None = None) -> str | None: ...

def save_to_buffer(string: str, buf: FilePath | WriteBuffer[str] | None = None, encoding: str | None = None) -> str | None: ...
def format_array(values: ArrayLike, formatter: Callable | None, float_format: FloatFormatType | None = None, na_rep: str = 'NaN', digits: int | None = None, space: str | int | None = None, justify: str = 'right', decimal: str = '.', leading_space: bool | None = True, quoting: int | None = None, fallback_formatter: Callable | None = None) -> list[str]: ...

class _GenericArrayFormatter:
    values: Incomplete
    digits: Incomplete
    na_rep: Incomplete
    space: Incomplete
    formatter: Incomplete
    float_format: Incomplete
    justify: Incomplete
    decimal: Incomplete
    quoting: Incomplete
    fixed_width: Incomplete
    leading_space: Incomplete
    fallback_formatter: Incomplete
    def __init__(self, values: ArrayLike, digits: int = 7, formatter: Callable | None = None, na_rep: str = 'NaN', space: str | int = 12, float_format: FloatFormatType | None = None, justify: str = 'right', decimal: str = '.', quoting: int | None = None, fixed_width: bool = True, leading_space: bool | None = True, fallback_formatter: Callable | None = None) -> None: ...
    def get_result(self) -> list[str]: ...

class FloatArrayFormatter(_GenericArrayFormatter):
    fixed_width: bool
    formatter: Incomplete
    float_format: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_result_as_array(self) -> np.ndarray: ...

class _IntArrayFormatter(_GenericArrayFormatter): ...

class _Datetime64Formatter(_GenericArrayFormatter):
    values: DatetimeArray
    nat_rep: Incomplete
    date_format: Incomplete
    def __init__(self, values: DatetimeArray, nat_rep: str = 'NaT', date_format: None = None, **kwargs) -> None: ...

class _ExtensionArrayFormatter(_GenericArrayFormatter):
    values: ExtensionArray

def format_percentiles(percentiles: np.ndarray | Sequence[float]) -> list[str]: ...
def get_precision(array: np.ndarray | Sequence[float]) -> int: ...
def get_format_datetime64(is_dates_only: bool, nat_rep: str = 'NaT', date_format: str | None = None) -> Callable: ...

class _Datetime64TZFormatter(_Datetime64Formatter):
    values: DatetimeArray

class _Timedelta64Formatter(_GenericArrayFormatter):
    values: TimedeltaArray
    nat_rep: Incomplete
    def __init__(self, values: TimedeltaArray, nat_rep: str = 'NaT', **kwargs) -> None: ...

def get_format_timedelta64(values: TimedeltaArray, nat_rep: str | float = 'NaT', box: bool = False) -> Callable: ...

class EngFormatter:
    ENG_PREFIXES: Incomplete
    accuracy: Incomplete
    use_eng_prefix: Incomplete
    def __init__(self, accuracy: int | None = None, use_eng_prefix: bool = False) -> None: ...
    def __call__(self, num: float) -> str: ...

def set_eng_float_format(accuracy: int = 3, use_eng_prefix: bool = False) -> None: ...
def get_level_lengths(levels: Any, sentinel: bool | object | str = '') -> list[dict[int, int]]: ...
def buffer_put_lines(buf: WriteBuffer[str], lines: list[str]) -> None: ...
