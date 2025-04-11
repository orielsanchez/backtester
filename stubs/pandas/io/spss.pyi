from collections.abc import Sequence
from pandas import DataFrame as DataFrame
from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.inference import is_list_like as is_list_like
from pandas.io.common import stringify_path as stringify_path
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from pathlib import Path

def read_spss(path: str | Path, usecols: Sequence[str] | None = None, convert_categoricals: bool = True, dtype_backend: DtypeBackend | lib.NoDefault = ...) -> DataFrame: ...
