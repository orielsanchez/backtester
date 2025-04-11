from _typeshed import Incomplete
from numpy import intp as c_intp

__all__ = ['load_library', 'ndpointer', 'c_intp', 'as_ctypes', 'as_array', 'as_ctypes_type']

load_library: Incomplete
as_ctypes: Incomplete
as_array: Incomplete

class _ndptr(_ndptr_base):
    @classmethod
    def from_param(cls, obj): ...

class _concrete_ndptr(_ndptr):
    @property
    def contents(self): ...

def ndpointer(dtype: Incomplete | None = None, ndim: Incomplete | None = None, shape: Incomplete | None = None, flags: Incomplete | None = None): ...
def as_ctypes_type(dtype): ...
