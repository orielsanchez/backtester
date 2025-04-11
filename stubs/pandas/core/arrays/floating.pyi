import numpy as np
from _typeshed import Incomplete
from pandas.core.arrays.numeric import NumericArray as NumericArray, NumericDtype as NumericDtype
from pandas.core.dtypes.base import register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.common import is_float_dtype as is_float_dtype
from typing import ClassVar

class FloatingDtype(NumericDtype):
    @classmethod
    def construct_array_type(cls) -> type[FloatingArray]: ...

class FloatingArray(NumericArray): ...

class Float32Dtype(FloatingDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class Float64Dtype(FloatingDtype):
    type = np.float64
    name: ClassVar[str]
    __doc__: Incomplete

NUMPY_FLOAT_TO_DTYPE: dict[np.dtype, FloatingDtype]
