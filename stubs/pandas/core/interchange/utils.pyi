import pandas as pd
from _typeshed import Incomplete
from pandas._libs import lib as lib
from pandas._typing import DtypeObj as DtypeObj
from pandas.core.dtypes.dtypes import ArrowDtype as ArrowDtype, CategoricalDtype as CategoricalDtype, DatetimeTZDtype as DatetimeTZDtype

PYARROW_CTYPES: Incomplete

class ArrowCTypes:
    NULL: str
    BOOL: str
    INT8: str
    UINT8: str
    INT16: str
    UINT16: str
    INT32: str
    UINT32: str
    INT64: str
    UINT64: str
    FLOAT16: str
    FLOAT32: str
    FLOAT64: str
    STRING: str
    LARGE_STRING: str
    DATE32: str
    DATE64: str
    TIMESTAMP: str
    TIME: str

class Endianness:
    LITTLE: str
    BIG: str
    NATIVE: str
    NA: str

def dtype_to_arrow_c_fmt(dtype: DtypeObj) -> str: ...
def maybe_rechunk(series: pd.Series, *, allow_copy: bool) -> pd.Series | None: ...
