from ._multiarray_umath import *
from ._multiarray_umath import _ARRAY_API as _ARRAY_API, _flagdict as _flagdict, _monotonicity as _monotonicity, _place as _place, _reconstruct as _reconstruct, _vec_string as _vec_string, from_dlpack as from_dlpack
from _typeshed import Incomplete

__all__ = ['_ARRAY_API', 'ALLOW_THREADS', 'BUFSIZE', 'CLIP', 'DATETIMEUNITS', 'ITEM_HASOBJECT', 'ITEM_IS_POINTER', 'LIST_PICKLE', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'NEEDS_INIT', 'NEEDS_PYAPI', 'RAISE', 'USE_GETITEM', 'USE_SETITEM', 'WRAP', '_flagdict', 'from_dlpack', '_place', '_reconstruct', '_vec_string', '_monotonicity', 'add_docstring', 'arange', 'array', 'asarray', 'asanyarray', 'ascontiguousarray', 'asfortranarray', 'bincount', 'broadcast', 'busday_count', 'busday_offset', 'busdaycalendar', 'can_cast', 'compare_chararrays', 'concatenate', 'copyto', 'correlate', 'correlate2', 'count_nonzero', 'c_einsum', 'datetime_as_string', 'datetime_data', 'dot', 'dragon4_positional', 'dragon4_scientific', 'dtype', 'empty', 'empty_like', 'error', 'flagsobj', 'flatiter', 'format_longfloat', 'frombuffer', 'fromfile', 'fromiter', 'fromstring', 'get_handler_name', 'get_handler_version', 'inner', 'interp', 'interp_complex', 'is_busday', 'lexsort', 'matmul', 'vecdot', 'may_share_memory', 'min_scalar_type', 'ndarray', 'nditer', 'nested_iters', 'normalize_axis_index', 'packbits', 'promote_types', 'putmask', 'ravel_multi_index', 'result_type', 'scalar', 'set_datetimeparse_function', 'set_typeDict', 'shares_memory', 'typeinfo', 'unpackbits', 'unravel_index', 'vdot', 'where', 'zeros']

def empty_like(prototype, dtype: Incomplete | None = None, order: Incomplete | None = None, subok: Incomplete | None = None, shape: Incomplete | None = None, *, device: Incomplete | None = None): ...
def concatenate(arrays, axis: Incomplete | None = None, out: Incomplete | None = None, *, dtype: Incomplete | None = None, casting: Incomplete | None = None): ...
def inner(a, b): ...
def where(condition, x: Incomplete | None = None, y: Incomplete | None = None): ...
def lexsort(keys, axis: Incomplete | None = None): ...
def can_cast(from_, to, casting: Incomplete | None = None): ...
def min_scalar_type(a): ...
def result_type(*arrays_and_dtypes): ...
def dot(a, b, out: Incomplete | None = None): ...
def vdot(a, b): ...
def bincount(x, weights: Incomplete | None = None, minlength: Incomplete | None = None): ...
def ravel_multi_index(multi_index, dims, mode: Incomplete | None = None, order: Incomplete | None = None): ...
def unravel_index(indices, shape: Incomplete | None = None, order: Incomplete | None = None): ...
def copyto(dst, src, casting: Incomplete | None = None, where: Incomplete | None = None): ...
def putmask(a, /, mask, values): ...
def packbits(a, axis: Incomplete | None = None, bitorder: str = 'big'): ...
def unpackbits(a, axis: Incomplete | None = None, count: Incomplete | None = None, bitorder: str = 'big'): ...
def shares_memory(a, b, max_work: Incomplete | None = None): ...
def may_share_memory(a, b, max_work: Incomplete | None = None): ...
def is_busday(dates, weekmask: Incomplete | None = None, holidays: Incomplete | None = None, busdaycal: Incomplete | None = None, out: Incomplete | None = None): ...
def busday_offset(dates, offsets, roll: Incomplete | None = None, weekmask: Incomplete | None = None, holidays: Incomplete | None = None, busdaycal: Incomplete | None = None, out: Incomplete | None = None): ...
def busday_count(begindates, enddates, weekmask: Incomplete | None = None, holidays: Incomplete | None = None, busdaycal: Incomplete | None = None, out: Incomplete | None = None): ...
def datetime_as_string(arr, unit: Incomplete | None = None, timezone: Incomplete | None = None, casting: Incomplete | None = None): ...

# Names in __all__ with no definition:
#   ALLOW_THREADS
#   BUFSIZE
#   CLIP
#   DATETIMEUNITS
#   ITEM_HASOBJECT
#   ITEM_IS_POINTER
#   LIST_PICKLE
#   MAXDIMS
#   MAY_SHARE_BOUNDS
#   MAY_SHARE_EXACT
#   NEEDS_INIT
#   NEEDS_PYAPI
#   RAISE
#   USE_GETITEM
#   USE_SETITEM
#   WRAP
#   add_docstring
#   arange
#   array
#   asanyarray
#   asarray
#   ascontiguousarray
#   asfortranarray
#   broadcast
#   busdaycalendar
#   c_einsum
#   compare_chararrays
#   correlate
#   correlate2
#   count_nonzero
#   datetime_data
#   dragon4_positional
#   dragon4_scientific
#   dtype
#   empty
#   error
#   flagsobj
#   flatiter
#   format_longfloat
#   frombuffer
#   fromfile
#   fromiter
#   fromstring
#   get_handler_name
#   get_handler_version
#   interp
#   interp_complex
#   matmul
#   ndarray
#   nditer
#   nested_iters
#   normalize_axis_index
#   promote_types
#   scalar
#   set_datetimeparse_function
#   set_typeDict
#   typeinfo
#   vecdot
#   zeros
