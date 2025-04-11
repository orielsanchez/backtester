import _cython_3_0_11
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op as maybe_dispatch_ufunc_to_dunder_op
from typing import ClassVar

NA: NAType
__pyx_capi__: dict
__test__: dict
check_na_tuples_nonequal: _cython_3_0_11.cython_function_or_method
checknull: _cython_3_0_11.cython_function_or_method
is_matching_na: _cython_3_0_11.cython_function_or_method
is_numeric_na: _cython_3_0_11.cython_function_or_method
isnaobj: _cython_3_0_11.cython_function_or_method
isneginf_scalar: _cython_3_0_11.cython_function_or_method
isposinf_scalar: _cython_3_0_11.cython_function_or_method
maxsize: int

class C_NAType:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...

class NAType(C_NAType):
    _HANDLED_TYPES: ClassVar[tuple] = ...
    _instance: ClassVar[NAType] = ...
    __array_priority__: ClassVar[int] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __abs__(self): ...
    def __add__(self, other): ...
    def __and__(self, other): ...
    def __array_ufunc__(self, *args, **kwargs): ...
    def __bool__(self) -> bool: ...
    def __divmod__(self, other): ...
    def __eq__(self, other: object) -> bool: ...
    def __floordiv__(self, other): ...
    def __format__(self, *args, **kwargs) -> str: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __invert__(self): ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __matmul__(self, *args, **kwargs): ...
    def __mod__(self, other): ...
    def __mul__(self, other): ...
    def __ne__(self, other: object) -> bool: ...
    def __neg__(self): ...
    def __or__(self, other): ...
    def __pos__(self): ...
    def __pow__(self, other): ...
    def __radd__(self, other): ...
    def __rand__(self, other): ...
    def __rdivmod__(self, other): ...
    def __reduce__(self): ...
    def __rfloordiv__(self, other): ...
    def __rmatmul__(self, *args, **kwargs): ...
    def __rmod__(self, other): ...
    def __rmul__(self, other): ...
    def __ror__(self, other): ...
    def __rpow__(self, other): ...
    def __rsub__(self, other): ...
    def __rtruediv__(self, other): ...
    def __rxor__(self, other): ...
    def __sub__(self, other): ...
    def __truediv__(self, other): ...
    def __xor__(self, other): ...
