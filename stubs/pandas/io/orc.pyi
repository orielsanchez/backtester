import fsspec
import pyarrow
import pyarrow.fs
from pandas._config import using_pyarrow_string_dtype as using_pyarrow_string_dtype
from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend, FilePath as FilePath, ReadBuffer as ReadBuffer, WriteBuffer as WriteBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.api import default_index as default_index
from pandas.io._util import arrow_string_types_mapper as arrow_string_types_mapper
from pandas.io.common import get_handle as get_handle, is_fsspec_url as is_fsspec_url
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from typing import Any, Literal

def read_orc(path: FilePath | ReadBuffer[bytes], columns: list[str] | None = None, dtype_backend: DtypeBackend | lib.NoDefault = ..., filesystem: pyarrow.fs.FileSystem | fsspec.spec.AbstractFileSystem | None = None, **kwargs: Any) -> DataFrame: ...
def to_orc(df: DataFrame, path: FilePath | WriteBuffer[bytes] | None = None, *, engine: Literal['pyarrow'] = 'pyarrow', index: bool | None = None, engine_kwargs: dict[str, Any] | None = None) -> bytes | None: ...
