import numpy as np
from _typeshed import Incomplete
from collections import abc
from pandas import DataFrame as DataFrame, Timestamp as Timestamp, isna as isna
from pandas._libs.byteswap import read_double_with_byteswap as read_double_with_byteswap, read_float_with_byteswap as read_float_with_byteswap, read_uint16_with_byteswap as read_uint16_with_byteswap, read_uint32_with_byteswap as read_uint32_with_byteswap, read_uint64_with_byteswap as read_uint64_with_byteswap
from pandas._libs.sas import Parser as Parser, get_subheader_index as get_subheader_index
from pandas._libs.tslibs.conversion import cast_from_unit_vectorized as cast_from_unit_vectorized
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.errors import EmptyDataError as EmptyDataError
from pandas.io.common import get_handle as get_handle
from pandas.io.sas.sasreader import ReaderBase as ReaderBase

class _Column:
    col_id: int
    name: str | bytes
    label: str | bytes
    format: str | bytes
    ctype: bytes
    length: int
    def __init__(self, col_id: int, name: str | bytes, label: str | bytes, format: str | bytes, ctype: bytes, length: int) -> None: ...

class SAS7BDATReader(ReaderBase, abc.Iterator):
    index: Incomplete
    convert_dates: Incomplete
    blank_missing: Incomplete
    chunksize: Incomplete
    encoding: Incomplete
    convert_text: Incomplete
    convert_header_text: Incomplete
    default_encoding: str
    compression: bytes
    column_names_raw: list[bytes]
    column_names: list[str | bytes]
    column_formats: list[str | bytes]
    columns: list[_Column]
    handles: Incomplete
    def __init__(self, path_or_buf: FilePath | ReadBuffer[bytes], index: Incomplete | None = None, convert_dates: bool = True, blank_missing: bool = True, chunksize: int | None = None, encoding: str | None = None, convert_text: bool = True, convert_header_text: bool = True, compression: CompressionOptions = 'infer') -> None: ...
    def column_data_lengths(self) -> np.ndarray: ...
    def column_data_offsets(self) -> np.ndarray: ...
    def column_types(self) -> np.ndarray: ...
    def close(self) -> None: ...
    def __next__(self) -> DataFrame: ...
    def read(self, nrows: int | None = None) -> DataFrame: ...
