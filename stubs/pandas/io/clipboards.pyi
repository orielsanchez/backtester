from pandas import get_option as get_option, option_context as option_context
from pandas._libs import lib as lib
from pandas._typing import DtypeBackend as DtypeBackend
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend

def read_clipboard(sep: str = '\\s+', dtype_backend: DtypeBackend | lib.NoDefault = ..., **kwargs): ...
def to_clipboard(obj, excel: bool | None = True, sep: str | None = None, **kwargs) -> None: ...
