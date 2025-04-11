from _typeshed import Incomplete
from numpy._core.multiarray import ravel_multi_index as ravel_multi_index, unravel_index as unravel_index

__all__ = ['ravel_multi_index', 'unravel_index', 'mgrid', 'ogrid', 'r_', 'c_', 's_', 'index_exp', 'ix_', 'ndenumerate', 'ndindex', 'fill_diagonal', 'diag_indices', 'diag_indices_from']

def ix_(*args): ...

class nd_grid:
    sparse: Incomplete
    def __init__(self, sparse: bool = False) -> None: ...
    def __getitem__(self, key): ...

class MGridClass(nd_grid):
    def __init__(self) -> None: ...

mgrid: Incomplete

class OGridClass(nd_grid):
    def __init__(self) -> None: ...

ogrid: Incomplete

class AxisConcatenator:
    concatenate: Incomplete
    makemat: Incomplete
    axis: Incomplete
    matrix: Incomplete
    trans1d: Incomplete
    ndmin: Incomplete
    def __init__(self, axis: int = 0, matrix: bool = False, ndmin: int = 1, trans1d: int = -1) -> None: ...
    def __getitem__(self, key): ...
    def __len__(self) -> int: ...

class RClass(AxisConcatenator):
    def __init__(self) -> None: ...

r_: Incomplete

class CClass(AxisConcatenator):
    def __init__(self) -> None: ...

c_: Incomplete

class ndenumerate:
    iter: Incomplete
    def __init__(self, arr) -> None: ...
    def __next__(self): ...
    def __iter__(self): ...

class ndindex:
    def __init__(self, *shape) -> None: ...
    def __iter__(self): ...
    def ndincr(self) -> None: ...
    def __next__(self): ...

class IndexExpression:
    maketuple: Incomplete
    def __init__(self, maketuple) -> None: ...
    def __getitem__(self, item): ...

index_exp: Incomplete
s_: Incomplete

def fill_diagonal(a, val, wrap: bool = False) -> None: ...
def diag_indices(n, ndim: int = 2): ...
def diag_indices_from(arr): ...
