from .numeric import dtype, ndarray
from _typeshed import Incomplete

__all__ = ['memmap']

dtypedescr = dtype

class memmap(ndarray):
    __array_priority__: float
    offset: Incomplete
    mode: Incomplete
    filename: Incomplete
    def __new__(subtype, filename, dtype=..., mode: str = 'r+', offset: int = 0, shape: Incomplete | None = None, order: str = 'C'): ...
    def __array_finalize__(self, obj) -> None: ...
    def flush(self) -> None: ...
    def __array_wrap__(self, arr, context: Incomplete | None = None, return_scalar: bool = False): ...
    def __getitem__(self, index): ...
