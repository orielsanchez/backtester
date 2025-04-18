from _typeshed import Incomplete

__all__ = ['nansum', 'nanmax', 'nanmin', 'nanargmax', 'nanargmin', 'nanmean', 'nanmedian', 'nanpercentile', 'nanvar', 'nanstd', 'nanprod', 'nancumsum', 'nancumprod', 'nanquantile']

def nanmin(a, axis: Incomplete | None = None, out: Incomplete | None = None, keepdims=..., initial=..., where=...): ...
def nanmax(a, axis: Incomplete | None = None, out: Incomplete | None = None, keepdims=..., initial=..., where=...): ...
def nanargmin(a, axis: Incomplete | None = None, out: Incomplete | None = None, *, keepdims=...): ...
def nanargmax(a, axis: Incomplete | None = None, out: Incomplete | None = None, *, keepdims=...): ...
def nansum(a, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None, keepdims=..., initial=..., where=...): ...
def nanprod(a, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None, keepdims=..., initial=..., where=...): ...
def nancumsum(a, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None): ...
def nancumprod(a, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None): ...
def nanmean(a, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None, keepdims=..., *, where=...): ...
def nanmedian(a, axis: Incomplete | None = None, out: Incomplete | None = None, overwrite_input: bool = False, keepdims=...): ...
def nanpercentile(a, q, axis: Incomplete | None = None, out: Incomplete | None = None, overwrite_input: bool = False, method: str = 'linear', keepdims=..., *, weights: Incomplete | None = None, interpolation: Incomplete | None = None): ...
def nanquantile(a, q, axis: Incomplete | None = None, out: Incomplete | None = None, overwrite_input: bool = False, method: str = 'linear', keepdims=..., *, weights: Incomplete | None = None, interpolation: Incomplete | None = None): ...
def nanvar(a, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None, ddof: int = 0, keepdims=..., *, where=..., mean=..., correction=...): ...
def nanstd(a, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None, ddof: int = 0, keepdims=..., *, where=..., mean=..., correction=...): ...
