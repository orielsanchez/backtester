import io
from _typeshed import Incomplete
from collections.abc import Sequence
from lxml import etree as etree
from pandas import DataFrame as DataFrame
from pandas._libs import lib as lib
from pandas._typing import CompressionOptions as CompressionOptions, ConvertersArg as ConvertersArg, DtypeArg as DtypeArg, DtypeBackend as DtypeBackend, FilePath as FilePath, ParseDatesArg as ParseDatesArg, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, XMLParsers as XMLParsers
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.errors import AbstractMethodError as AbstractMethodError, ParserError as ParserError
from pandas.io.common import file_exists as file_exists, get_handle as get_handle, infer_compression as infer_compression, is_file_like as is_file_like, is_fsspec_url as is_fsspec_url, is_url as is_url, stringify_path as stringify_path
from pandas.io.parsers import TextParser as TextParser
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend

class _XMLFrameParser:
    path_or_buffer: Incomplete
    xpath: Incomplete
    namespaces: Incomplete
    elems_only: Incomplete
    attrs_only: Incomplete
    names: Incomplete
    dtype: Incomplete
    converters: Incomplete
    parse_dates: Incomplete
    encoding: Incomplete
    stylesheet: Incomplete
    iterparse: Incomplete
    is_style: Incomplete
    compression: CompressionOptions
    storage_options: Incomplete
    def __init__(self, path_or_buffer: FilePath | ReadBuffer[bytes] | ReadBuffer[str], xpath: str, namespaces: dict[str, str] | None, elems_only: bool, attrs_only: bool, names: Sequence[str] | None, dtype: DtypeArg | None, converters: ConvertersArg | None, parse_dates: ParseDatesArg | None, encoding: str | None, stylesheet: FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None, iterparse: dict[str, list[str]] | None, compression: CompressionOptions, storage_options: StorageOptions) -> None: ...
    def parse_data(self) -> list[dict[str, str | None]]: ...

class _EtreeFrameParser(_XMLFrameParser):
    xml_doc: Incomplete
    def parse_data(self) -> list[dict[str, str | None]]: ...

class _LxmlFrameParser(_XMLFrameParser):
    xml_doc: Incomplete
    xsl_doc: Incomplete
    def parse_data(self) -> list[dict[str, str | None]]: ...

def get_data_from_filepath(filepath_or_buffer: FilePath | bytes | ReadBuffer[bytes] | ReadBuffer[str], encoding: str | None, compression: CompressionOptions, storage_options: StorageOptions) -> str | bytes | ReadBuffer[bytes] | ReadBuffer[str]: ...
def preprocess_data(data) -> io.StringIO | io.BytesIO: ...
def read_xml(path_or_buffer: FilePath | ReadBuffer[bytes] | ReadBuffer[str], *, xpath: str = './*', namespaces: dict[str, str] | None = None, elems_only: bool = False, attrs_only: bool = False, names: Sequence[str] | None = None, dtype: DtypeArg | None = None, converters: ConvertersArg | None = None, parse_dates: ParseDatesArg | None = None, encoding: str | None = 'utf-8', parser: XMLParsers = 'lxml', stylesheet: FilePath | ReadBuffer[bytes] | ReadBuffer[str] | None = None, iterparse: dict[str, list[str]] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None, dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
