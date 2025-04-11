from _typeshed import Incomplete

__all__ = ['atleast_1d', 'atleast_2d', 'atleast_3d', 'block', 'hstack', 'stack', 'unstack', 'vstack']

def atleast_1d(*arys): ...
def atleast_2d(*arys): ...
def atleast_3d(*arys): ...
def vstack(tup, *, dtype: Incomplete | None = None, casting: str = 'same_kind'): ...
def hstack(tup, *, dtype: Incomplete | None = None, casting: str = 'same_kind'): ...
def stack(arrays, axis: int = 0, out: Incomplete | None = None, *, dtype: Incomplete | None = None, casting: str = 'same_kind'): ...
def unstack(x, /, *, axis: int = 0): ...
def block(arrays): ...
