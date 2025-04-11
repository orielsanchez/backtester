from _typeshed import Incomplete

__all__ = ['finfo', 'iinfo']

class MachArLike:
    params: Incomplete
    ftype: Incomplete
    title: Incomplete
    epsilon: Incomplete
    epsneg: Incomplete
    xmax: Incomplete
    xmin: Incomplete
    smallest_normal: Incomplete
    ibeta: Incomplete
    precision: Incomplete
    resolution: Incomplete
    def __init__(self, ftype, *, eps, epsneg, huge, tiny, ibeta, smallest_subnormal: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def smallest_subnormal(self): ...

class finfo:
    __class_getitem__: Incomplete
    def __new__(cls, dtype): ...
    @property
    def smallest_normal(self): ...
    @property
    def tiny(self): ...

class iinfo:
    __class_getitem__: Incomplete
    dtype: Incomplete
    kind: Incomplete
    bits: Incomplete
    key: Incomplete
    def __init__(self, int_type) -> None: ...
    @property
    def min(self): ...
    @property
    def max(self): ...
