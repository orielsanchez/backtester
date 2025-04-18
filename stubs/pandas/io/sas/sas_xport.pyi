import pandas as pd
from _typeshed import Incomplete
from collections import abc
from pandas._typing import CompressionOptions as CompressionOptions, DatetimeNaTType as DatetimeNaTType, FilePath as FilePath, ReadBuffer as ReadBuffer
from pandas.io.common import get_handle as get_handle
from pandas.io.sas.sasreader import ReaderBase as ReaderBase
from pandas.util._decorators import Appender as Appender
from pandas.util._exceptions import find_stack_level as find_stack_level

class XportReader(ReaderBase, abc.Iterator):
    __doc__: Incomplete
    handles: Incomplete
    filepath_or_buffer: Incomplete
    def __init__(self, filepath_or_buffer: FilePath | ReadBuffer[bytes], index: Incomplete | None = None, encoding: str | None = 'ISO-8859-1', chunksize: int | None = None, compression: CompressionOptions = 'infer') -> None: ...
    def close(self) -> None: ...
    def __next__(self) -> pd.DataFrame: ...
    def get_chunk(self, size: int | None = None) -> pd.DataFrame: ...
    def read(self, nrows: int | None = None) -> pd.DataFrame: ...
