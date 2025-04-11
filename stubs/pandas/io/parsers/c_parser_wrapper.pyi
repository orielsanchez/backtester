from _typeshed import Incomplete
from collections.abc import Hashable, Mapping, Sequence
from pandas import Index as Index, MultiIndex as MultiIndex
from pandas._libs import lib as lib, parsers as parsers
from pandas._typing import ArrayLike as ArrayLike, DtypeArg as DtypeArg, DtypeObj as DtypeObj, ReadCsvBuffer as ReadCsvBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import pandas_dtype as pandas_dtype
from pandas.core.dtypes.concat import concat_compat as concat_compat, union_categoricals as union_categoricals
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.indexes.api import ensure_index_from_sequences as ensure_index_from_sequences
from pandas.errors import DtypeWarning as DtypeWarning
from pandas.io.common import dedup_names as dedup_names, is_potential_multi_index as is_potential_multi_index
from pandas.io.parsers.base_parser import ParserBase as ParserBase, ParserError as ParserError, is_index_col as is_index_col
from pandas.util._exceptions import find_stack_level as find_stack_level

class CParserWrapper(ParserBase):
    low_memory: bool
    kwds: Incomplete
    unnamed_cols: Incomplete
    names: Incomplete
    orig_names: Incomplete
    index_names: Incomplete
    def __init__(self, src: ReadCsvBuffer[str], **kwds) -> None: ...
    def close(self) -> None: ...
    def read(self, nrows: int | None = None) -> tuple[Index | MultiIndex | None, Sequence[Hashable] | MultiIndex, Mapping[Hashable, ArrayLike]]: ...

def ensure_dtype_objs(dtype: DtypeArg | dict[Hashable, DtypeArg] | None) -> DtypeObj | dict[Hashable, DtypeObj] | None: ...
