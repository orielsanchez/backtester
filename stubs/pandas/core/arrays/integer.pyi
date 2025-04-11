import numpy as np
from _typeshed import Incomplete
from pandas.core.arrays.numeric import NumericArray as NumericArray, NumericDtype as NumericDtype
from pandas.core.dtypes.base import register_extension_dtype as register_extension_dtype
from pandas.core.dtypes.common import is_integer_dtype as is_integer_dtype
from typing import ClassVar

class IntegerDtype(NumericDtype):
    @classmethod
    def construct_array_type(cls) -> type[IntegerArray]: ...

class IntegerArray(NumericArray): ...

class Int8Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class Int16Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class Int32Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class Int64Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class UInt8Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class UInt16Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class UInt32Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

class UInt64Dtype(IntegerDtype):
    type: Incomplete
    name: ClassVar[str]
    __doc__: Incomplete

NUMPY_INT_TO_DTYPE: dict[np.dtype, IntegerDtype]
