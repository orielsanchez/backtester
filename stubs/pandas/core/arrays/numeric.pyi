import numpy as np
import pyarrow
from pandas._libs import lib as lib
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, Self as Self, npt as npt
from pandas.core.arrays.masked import BaseMaskedArray as BaseMaskedArray, BaseMaskedDtype as BaseMaskedDtype
from pandas.core.dtypes.common import is_integer_dtype as is_integer_dtype, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.util._decorators import cache_readonly as cache_readonly

class NumericDtype(BaseMaskedDtype):
    def is_signed_integer(self) -> bool: ...
    def is_unsigned_integer(self) -> bool: ...
    def __from_arrow__(self, array: pyarrow.Array | pyarrow.ChunkedArray) -> BaseMaskedArray: ...

class NumericArray(BaseMaskedArray):
    def __init__(self, values: np.ndarray, mask: npt.NDArray[np.bool_], copy: bool = False) -> None: ...
    def dtype(self) -> NumericDtype: ...
