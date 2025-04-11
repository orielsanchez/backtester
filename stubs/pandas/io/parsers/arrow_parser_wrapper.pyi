from _typeshed import Incomplete
from pandas import DataFrame as DataFrame
from pandas._config import using_pyarrow_string_dtype as using_pyarrow_string_dtype
from pandas._libs import lib as lib
from pandas._typing import ReadBuffer as ReadBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import pandas_dtype as pandas_dtype
from pandas.core.dtypes.inference import is_integer as is_integer
from pandas.errors import ParserError as ParserError, ParserWarning as ParserWarning
from pandas.io._util import arrow_string_types_mapper as arrow_string_types_mapper
from pandas.io.parsers.base_parser import ParserBase as ParserBase
from pandas.util._exceptions import find_stack_level as find_stack_level

class ArrowParserWrapper(ParserBase):
    kwds: Incomplete
    src: Incomplete
    def __init__(self, src: ReadBuffer[bytes], **kwds) -> None: ...
    def read(self) -> DataFrame: ...
