from _typeshed import Incomplete
from collections.abc import Iterable, Sequence
from pandas import DataFrame as DataFrame, isna as isna
from pandas._libs import lib as lib
from pandas._typing import BaseBuffer as BaseBuffer, DtypeBackend as DtypeBackend, FilePath as FilePath, HTMLFlavors as HTMLFlavors, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.indexes.base import Index as Index
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.core.series import Series as Series
from pandas.errors import AbstractMethodError as AbstractMethodError, EmptyDataError as EmptyDataError
from pandas.io.common import file_exists as file_exists, get_handle as get_handle, is_file_like as is_file_like, is_fsspec_url as is_fsspec_url, is_url as is_url, stringify_path as stringify_path, validate_header_arg as validate_header_arg
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.io.parsers import TextParser as TextParser
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from re import Pattern
from typing import Literal

class _HtmlFrameParser:
    io: Incomplete
    match: Incomplete
    attrs: Incomplete
    encoding: Incomplete
    displayed_only: Incomplete
    extract_links: Incomplete
    storage_options: Incomplete
    def __init__(self, io: FilePath | ReadBuffer[str] | ReadBuffer[bytes], match: str | Pattern, attrs: dict[str, str] | None, encoding: str, displayed_only: bool, extract_links: Literal[None, 'header', 'footer', 'body', 'all'], storage_options: StorageOptions = None) -> None: ...
    def parse_tables(self): ...

class _BeautifulSoupHtml5LibFrameParser(_HtmlFrameParser): ...
class _LxmlFrameParser(_HtmlFrameParser): ...

def read_html(io: FilePath | ReadBuffer[str], *, match: str | Pattern = '.+', flavor: HTMLFlavors | Sequence[HTMLFlavors] | None = None, header: int | Sequence[int] | None = None, index_col: int | Sequence[int] | None = None, skiprows: int | Sequence[int] | slice | None = None, attrs: dict[str, str] | None = None, parse_dates: bool = False, thousands: str | None = ',', encoding: str | None = None, decimal: str = '.', converters: dict | None = None, na_values: Iterable[object] | None = None, keep_default_na: bool = True, displayed_only: bool = True, extract_links: Literal[None, 'header', 'footer', 'body', 'all'] = None, dtype_backend: DtypeBackend | lib.NoDefault = ..., storage_options: StorageOptions = None) -> list[DataFrame]: ...
