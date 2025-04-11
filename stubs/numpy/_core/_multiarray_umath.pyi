import numpy
from _typeshed import Incomplete
from numpy import absolute as absolute, add as add, arange as arange, arccos as arccos, arccosh as arccosh, arcsin as arcsin, arcsinh as arcsinh, arctan as arctan, arctan2 as arctan2, arctanh as arctanh, array as array, asanyarray as asanyarray, asarray as asarray, ascontiguousarray as ascontiguousarray, asfortranarray as asfortranarray, bitwise_and as bitwise_and, bitwise_count as bitwise_count, bitwise_or as bitwise_or, bitwise_xor as bitwise_xor, broadcast as broadcast, busdaycalendar as busdaycalendar, cbrt as cbrt, ceil as ceil, character as character, complexfloating as complexfloating, conj as conj, conjugate as conjugate, copysign as copysign, cos as cos, cosh as cosh, datetime_data as datetime_data, deg2rad as deg2rad, degrees as degrees, divide as divide, divmod as divmod, dtype as dtype, empty as empty, equal as equal, exp as exp, exp2 as exp2, expm1 as expm1, fabs as fabs, flatiter as flatiter, flexible as flexible, float_power as float_power, floating as floating, floor as floor, floor_divide as floor_divide, fmax as fmax, fmin as fmin, fmod as fmod, frexp as frexp, from_dlpack as from_dlpack, frombuffer as frombuffer, fromfile as fromfile, fromiter as fromiter, frompyfunc as frompyfunc, fromstring as fromstring, gcd as gcd, generic as generic, greater as greater, greater_equal as greater_equal, heaviside as heaviside, hypot as hypot, inexact as inexact, integer as integer, invert as invert, isfinite as isfinite, isinf as isinf, isnan as isnan, isnat as isnat, lcm as lcm, ldexp as ldexp, left_shift as left_shift, less as less, less_equal as less_equal, log as log, log10 as log10, log1p as log1p, log2 as log2, logaddexp as logaddexp, logaddexp2 as logaddexp2, logical_and as logical_and, logical_not as logical_not, logical_or as logical_or, logical_xor as logical_xor, matmul as matmul, matvec as matvec, maximum as maximum, may_share_memory as may_share_memory, minimum as minimum, mod as mod, modf as modf, multiply as multiply, ndarray as ndarray, nditer as nditer, negative as negative, nested_iters as nested_iters, nextafter as nextafter, not_equal as not_equal, number as number, positive as positive, power as power, promote_types as promote_types, rad2deg as rad2deg, radians as radians, reciprocal as reciprocal, remainder as remainder, right_shift as right_shift, rint as rint, sign as sign, signbit as signbit, signedinteger as signedinteger, sin as sin, sinh as sinh, spacing as spacing, sqrt as sqrt, square as square, subtract as subtract, tan as tan, tanh as tanh, true_divide as true_divide, trunc as trunc, unsignedinteger as unsignedinteger, vecdot as vecdot, vecmat as vecmat, zeros as zeros
from numpy._core.multiarray import flagsobj as flagsobj, scalar as scalar
from numpy.char import compare_chararrays as compare_chararrays
from numpy.dtypes import StringDType as StringDType
from numpy.lib import add_docstring as add_docstring
from numpy.lib.array_utils import normalize_axis_index as normalize_axis_index
from typing import Any, overload

ALLOW_THREADS: int
BUFSIZE: int
CLIP: int
DATETIMEUNITS: PyCapsule
FLOATING_POINT_SUPPORT: int
FPE_DIVIDEBYZERO: int
FPE_INVALID: int
FPE_OVERFLOW: int
FPE_UNDERFLOW: int
ITEM_HASOBJECT: int
ITEM_IS_POINTER: int
LIST_PICKLE: int
MAXDIMS: int
MAY_SHARE_BOUNDS: int
MAY_SHARE_EXACT: int
NAN: float
NEEDS_INIT: int
NEEDS_PYAPI: int
NINF: float
NZERO: float
PINF: float
PZERO: float
RAISE: int
UFUNC_BUFSIZE_DEFAULT: int
UFUNC_PYVALS_NAME: str
USE_GETITEM: int
USE_SETITEM: int
WRAP: int
__cpu_baseline__: list
__cpu_dispatch__: list
__cpu_features__: dict
__cpu_targets_info__: dict
__version__: str
clip: numpy.ufunc
count: numpy.ufunc
e: float
endswith: numpy.ufunc
euler_gamma: float
find: numpy.ufunc
index: numpy.ufunc
isalnum: numpy.ufunc
isalpha: numpy.ufunc
isdecimal: numpy.ufunc
isdigit: numpy.ufunc
islower: numpy.ufunc
isnumeric: numpy.ufunc
isspace: numpy.ufunc
istitle: numpy.ufunc
isupper: numpy.ufunc
pi: float
rfind: numpy.ufunc
rindex: numpy.ufunc
startswith: numpy.ufunc
str_len: numpy.ufunc
tracemalloc_domain: int
typeinfo: dict

class _array_converter:
    scalar_input: Incomplete
    @classmethod
    def __init__(cls, *array_likes) -> Any: ...
    def as_arrays(self, *args, **kwargs): ...
    def result_type(self, *args, **kwargs): ...
    def wrap(self, *args, **kwargs): ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...

@overload
def bincount(x) -> Any: ...
@overload
def bincount(x, weights=...) -> Any: ...
def busday_count(*args, **kwargs): ...
def busday_offset(*args, **kwargs): ...
def c_einsum(subscripts, *operands, out=..., dtype=..., order=..., 
casting=...) -> Any: ...
@overload
def can_cast(from_, to, casting=...) -> Any: ...
@overload
def can_cast(complex, float) -> Any: ...
def concatenate(*args, **kwargs): ...
@overload
def copyto(dst, src, casting=..., where=...) -> Any: ...
@overload
def copyto(A, B) -> Any: ...
@overload
def copyto(A, B) -> Any: ...
def correlate(*args, **kwargs): ...
def correlate2(*args, **kwargs): ...
def count_nonzero(*args, **kwargs): ...
@overload
def datetime_as_string(arr, unit=..., timezone=..., casting=...) -> Any: ...
@overload
def datetime_as_string(d, timezone=...) -> Any: ...
@overload
def datetime_as_string(d, timezone=...) -> Any: ...
@overload
def datetime_as_string(d, unit=...) -> Any: ...
@overload
def datetime_as_string(d, unit=...) -> Any: ...
@overload
def datetime_as_string(d, unit=..., casting=...) -> Any: ...
@overload
def dot(a, b, out=...) -> Any: ...
@overload
def dot(a, b) -> Any: ...
@overload
def dot(a, b) -> Any: ...
@overload
def dot(a, b) -> Any: ...
@overload
def dot(a, b) -> Any: ...
def dragon4_positional(*args, **kwargs): ...
def dragon4_scientific(*args, **kwargs): ...
@overload
def empty_like(a) -> Any: ...
@overload
def empty_like(a) -> Any: ...
def format_longfloat(*args, **kwargs): ...
def get_handler_name(*args, **kwargs): ...
def get_handler_version(*args, **kwargs): ...
@overload
def inner(a, b) -> Any: ...
@overload
def inner(a, b) -> Any: ...
@overload
def inner(a, b) -> Any: ...
@overload
def inner(a, b) -> Any: ...
@overload
def inner(a, b) -> Any: ...
@overload
def inner(a, b) -> Any: ...
@overload
def inner(a, b) -> Any: ...
def interp(*args, **kwargs): ...
def interp_complex(*args, **kwargs): ...
def is_busday(*args, **kwargs): ...
@overload
def lexsort(keys, axis=...) -> Any: ...
@overload
def lexsort(arr) -> Any: ...
def min_scalar_type(*args, **kwargs): ...
def packbits(a, axis=...) -> Any: ...
def putmask(a, mask, values) -> Any: ...
def ravel_multi_index(multi_index, dims, mode=..., order=...) -> Any: ...
def result_type(*arrays_and_dtypes) -> Any: ...
def set_datetimeparse_function(*args, **kwargs): ...
def set_typeDict(dict) -> Any: ...
@overload
def shares_memory(x1, x2, max_work=...) -> Any: ...
@overload
def shares_memory(x1, x2) -> Any: ...
@overload
def unpackbits(a, axis=...) -> Any: ...
@overload
def unpackbits(a, axis=..., count=...) -> Any: ...
@overload
def unpackbits(p, axis=...) -> Any: ...
@overload
def unpackbits(p, axis=..., count=...) -> Any: ...
def unravel_index(indices, shape, order=...) -> Any: ...
@overload
def vdot(a, b) -> Any: ...
@overload
def vdot(b, a) -> Any: ...
@overload
def vdot(a, b) -> Any: ...
@overload
def vdot(b, a) -> Any: ...
def where(*args, **kwargs): ...
