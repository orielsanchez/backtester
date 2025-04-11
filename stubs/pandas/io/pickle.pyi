from pandas import DataFrame as DataFrame, Series as Series
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadPickleBuffer as ReadPickleBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.io.common import get_handle as get_handle
from pandas.util._decorators import doc as doc
from typing import Any

def to_pickle(obj: Any, filepath_or_buffer: FilePath | WriteBuffer[bytes], compression: CompressionOptions = 'infer', protocol: int = ..., storage_options: StorageOptions | None = None) -> None: ...
def read_pickle(filepath_or_buffer: FilePath | ReadPickleBuffer, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None) -> DataFrame | Series: ...
