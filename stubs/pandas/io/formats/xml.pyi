from _typeshed import Incomplete
from pandas import DataFrame as DataFrame
from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.dtypes.missing import isna as isna
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import get_handle as get_handle
from pandas.io.xml import get_data_from_filepath as get_data_from_filepath, preprocess_data as preprocess_data
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc

class _BaseXMLFormatter:
    frame: Incomplete
    path_or_buffer: Incomplete
    index: Incomplete
    root_name: Incomplete
    row_name: Incomplete
    na_rep: Incomplete
    attr_cols: Incomplete
    elem_cols: Incomplete
    namespaces: Incomplete
    prefix: Incomplete
    encoding: Incomplete
    xml_declaration: Incomplete
    pretty_print: Incomplete
    stylesheet: Incomplete
    compression: CompressionOptions
    storage_options: Incomplete
    orig_cols: Incomplete
    frame_dicts: Incomplete
    prefix_uri: Incomplete
    def __init__(self, frame: DataFrame, path_or_buffer: FilePath | WriteBuffer[bytes] | WriteBuffer[str] | None = None, index: bool = True, root_name: str | None = 'data', row_name: str | None = 'row', na_rep: str | None = None, attr_cols: list[str] | None = None, elem_cols: list[str] | None = None, namespaces: dict[str | None, str] | None = None, prefix: str | None = None, encoding: str = 'utf-8', xml_declaration: bool | None = True, pretty_print: bool | None = True, stylesheet: FilePath | ReadBuffer[str] | ReadBuffer[bytes] | None = None, compression: CompressionOptions = 'infer', storage_options: StorageOptions | None = None) -> None: ...
    def write_output(self) -> str | None: ...

class EtreeXMLFormatter(_BaseXMLFormatter): ...

class LxmlXMLFormatter(_BaseXMLFormatter):
    def __init__(self, *args, **kwargs) -> None: ...
