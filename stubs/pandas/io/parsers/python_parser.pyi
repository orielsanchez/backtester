import re
from _typeshed import Incomplete
from collections import abc
from collections.abc import Hashable, Iterator, Mapping, Sequence
from pandas import Index as Index, MultiIndex as MultiIndex
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, ReadCsvBuffer as ReadCsvBuffer, Scalar as Scalar
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_integer as is_integer, is_numeric_dtype as is_numeric_dtype
from pandas.core.dtypes.inference import is_dict_like as is_dict_like
from pandas.errors import EmptyDataError as EmptyDataError, ParserError as ParserError, ParserWarning as ParserWarning
from pandas.io.common import dedup_names as dedup_names, is_potential_multi_index as is_potential_multi_index
from pandas.io.parsers.base_parser import ParserBase as ParserBase, parser_defaults as parser_defaults
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import IO, Literal

class PythonParser(ParserBase):
    data: Iterator[str] | None
    buf: list
    pos: int
    line_pos: int
    skiprows: Incomplete
    skipfunc: Incomplete
    skipfooter: Incomplete
    delimiter: Incomplete
    quotechar: Incomplete
    escapechar: Incomplete
    doublequote: Incomplete
    skipinitialspace: Incomplete
    lineterminator: Incomplete
    quoting: Incomplete
    skip_blank_lines: Incomplete
    has_index_names: bool
    verbose: Incomplete
    thousands: Incomplete
    decimal: Incomplete
    comment: Incomplete
    orig_names: list[Hashable]
    index_names: Incomplete
    def __init__(self, f: ReadCsvBuffer[str] | list, **kwds) -> None: ...
    def num(self) -> re.Pattern: ...
    def read(self, rows: int | None = None) -> tuple[Index | None, Sequence[Hashable] | MultiIndex, Mapping[Hashable, ArrayLike]]: ...
    def get_chunk(self, size: int | None = None) -> tuple[Index | None, Sequence[Hashable] | MultiIndex, Mapping[Hashable, ArrayLike]]: ...

class FixedWidthReader(abc.Iterator):
    f: Incomplete
    buffer: Iterator | None
    delimiter: Incomplete
    comment: Incomplete
    colspecs: Incomplete
    def __init__(self, f: IO[str] | ReadCsvBuffer[str], colspecs: list[tuple[int, int]] | Literal['infer'], delimiter: str | None, comment: str | None, skiprows: set[int] | None = None, infer_nrows: int = 100) -> None: ...
    def get_rows(self, infer_nrows: int, skiprows: set[int] | None = None) -> list[str]: ...
    def detect_colspecs(self, infer_nrows: int = 100, skiprows: set[int] | None = None) -> list[tuple[int, int]]: ...
    def __next__(self) -> list[str]: ...

class FixedWidthFieldParser(PythonParser):
    colspecs: Incomplete
    infer_nrows: Incomplete
    def __init__(self, f: ReadCsvBuffer[str], **kwds) -> None: ...

def count_empty_vals(vals) -> int: ...
