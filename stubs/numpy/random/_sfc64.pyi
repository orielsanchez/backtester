import _cython_3_0_12
import numpy as np
import numpy.random.bit_generator
from _typeshed import Incomplete
from typing import Any, ClassVar

__reduce_cython__: _cython_3_0_12.cython_function_or_method
__setstate_cython__: _cython_3_0_12.cython_function_or_method
__test__: dict

class SFC64(numpy.random.bit_generator.BitGenerator):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    state: Incomplete
    def __init__(self, seed=...) -> Any: ...
    def __reduce_cython__(self, *args, **kwargs): ...
    def __setstate_cython__(self, *args, **kwargs): ...
