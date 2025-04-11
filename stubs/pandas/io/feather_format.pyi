from collections.abc import Hashable, Sequence
from pandas._config import using_pyarrow_string_dtype as using_pyarrow_string_dtype
from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.api import DataFrame as DataFrame
from pandas.io._util import arrow_string_types_mapper as arrow_string_types_mapper
from pandas.io.common import get_handle as get_handle
from pandas.util._decorators import doc as doc
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from typing import Any

def to_feather(df: DataFrame, path: FilePath | WriteBuffer[bytes], storage_options: StorageOptions | None = None, **kwargs: Any) -> None: ...
def read_feather(path: FilePath | ReadBuffer[bytes], columns: Sequence[Hashable] | None = None, use_threads: bool = True, storage_options: StorageOptions | None = None, dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
