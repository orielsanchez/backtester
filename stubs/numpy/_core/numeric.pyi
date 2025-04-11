from .umath import *
from .numerictypes import *
from .fromnumeric import *
from .arrayprint import *
from ._asarray import *
from ._ufunc_config import *
from ._ufunc_config import errstate as errstate
from .multiarray import arange as arange, array as array, asanyarray as asanyarray, asarray as asarray, ascontiguousarray as ascontiguousarray, asfortranarray as asfortranarray, broadcast as broadcast, can_cast as can_cast, concatenate as concatenate, copyto as copyto, dot as dot, dtype as dtype, empty as empty, empty_like as empty_like, flatiter as flatiter, from_dlpack as from_dlpack, frombuffer as frombuffer, fromfile as fromfile, fromiter as fromiter, fromstring as fromstring, inner as inner, lexsort as lexsort, matmul as matmul, may_share_memory as may_share_memory, min_scalar_type as min_scalar_type, ndarray as ndarray, nditer as nditer, nested_iters as nested_iters, promote_types as promote_types, putmask as putmask, result_type as result_type, shares_memory as shares_memory, vdot as vdot, vecdot as vecdot, where as where, zeros as zeros
from .umath import NAN, PINF, invert as invert, multiply as multiply, sin as sin
from _typeshed import Incomplete

__all__ = ['newaxis', 'ndarray', 'flatiter', 'nditer', 'nested_iters', 'ufunc', 'arange', 'array', 'asarray', 'asanyarray', 'ascontiguousarray', 'asfortranarray', 'zeros', 'count_nonzero', 'empty', 'broadcast', 'dtype', 'fromstring', 'fromfile', 'frombuffer', 'from_dlpack', 'where', 'argwhere', 'copyto', 'concatenate', 'lexsort', 'astype', 'can_cast', 'promote_types', 'min_scalar_type', 'result_type', 'isfortran', 'empty_like', 'zeros_like', 'ones_like', 'correlate', 'convolve', 'inner', 'dot', 'outer', 'vdot', 'roll', 'rollaxis', 'moveaxis', 'cross', 'tensordot', 'little_endian', 'fromiter', 'array_equal', 'array_equiv', 'indices', 'fromfunction', 'isclose', 'isscalar', 'binary_repr', 'base_repr', 'ones', 'identity', 'allclose', 'putmask', 'flatnonzero', 'inf', 'nan', 'False_', 'True_', 'bitwise_not', 'full', 'full_like', 'matmul', 'vecdot', 'shares_memory', 'may_share_memory', 'all', 'amax', 'amin', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'around', 'choose', 'clip', 'compress', 'cumprod', 'cumsum', 'cumulative_prod', 'cumulative_sum', 'diagonal', 'mean', 'max', 'min', 'matrix_transpose', 'ndim', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'shape', 'size', 'sort', 'squeeze', 'std', 'sum', 'swapaxes', 'take', 'trace', 'transpose', 'var', 'absolute', 'add', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'bitwise_and', 'bitwise_or', 'bitwise_xor', 'cbrt', 'ceil', 'conj', 'conjugate', 'copysign', 'cos', 'cosh', 'bitwise_count', 'deg2rad', 'degrees', 'divide', 'divmod', 'e', 'equal', 'euler_gamma', 'exp', 'exp2', 'expm1', 'fabs', 'floor', 'floor_divide', 'float_power', 'fmax', 'fmin', 'fmod', 'frexp', 'frompyfunc', 'gcd', 'greater', 'greater_equal', 'heaviside', 'hypot', 'invert', 'isfinite', 'isinf', 'isnan', 'isnat', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'matvec', 'maximum', 'minimum', 'mod', 'modf', 'multiply', 'negative', 'nextafter', 'not_equal', 'pi', 'positive', 'power', 'rad2deg', 'radians', 'reciprocal', 'remainder', 'right_shift', 'rint', 'sign', 'signbit', 'sin', 'sinh', 'spacing', 'sqrt', 'square', 'subtract', 'tan', 'tanh', 'true_divide', 'trunc', 'vecmat', 'ScalarType', 'typecodes', 'issubdtype', 'datetime_data', 'datetime_as_string', 'busday_offset', 'busday_count', 'is_busday', 'busdaycalendar', 'isdtype', 'character', 'integer', 'generic', 'inexact', 'flexible', 'number', 'floating', 'signedinteger', 'unsignedinteger', 'complexfloating', 'bool', 'float16', 'float32', 'float64', 'longdouble', 'complex64', 'complex128', 'clongdouble', 'bytes_', 'str_', 'void', 'object_', 'datetime64', 'timedelta64', 'int8', 'byte', 'uint8', 'ubyte', 'int16', 'short', 'uint16', 'ushort', 'int32', 'intc', 'uint32', 'uintc', 'int64', 'long', 'uint64', 'ulong', 'longlong', 'ulonglong', 'intp', 'uintp', 'double', 'cdouble', 'single', 'csingle', 'half', 'bool_', 'int_', 'uint', 'array2string', 'array_str', 'array_repr', 'set_printoptions', 'get_printoptions', 'printoptions', 'format_float_positional', 'format_float_scientific', 'require', 'seterr', 'geterr', 'setbufsize', 'getbufsize', 'seterrcall', 'geterrcall', 'errstate']

bitwise_not = invert
ufunc: Incomplete
newaxis: Incomplete

def zeros_like(a, dtype: Incomplete | None = None, order: str = 'K', subok: bool = True, shape: Incomplete | None = None, *, device: Incomplete | None = None): ...
def ones(shape, dtype: Incomplete | None = None, order: str = 'C', *, device: Incomplete | None = None, like: Incomplete | None = None): ...
def ones_like(a, dtype: Incomplete | None = None, order: str = 'K', subok: bool = True, shape: Incomplete | None = None, *, device: Incomplete | None = None): ...
def full(shape, fill_value, dtype: Incomplete | None = None, order: str = 'C', *, device: Incomplete | None = None, like: Incomplete | None = None): ...
def full_like(a, fill_value, dtype: Incomplete | None = None, order: str = 'K', subok: bool = True, shape: Incomplete | None = None, *, device: Incomplete | None = None): ...
def count_nonzero(a, axis: Incomplete | None = None, *, keepdims: bool = False): ...
def isfortran(a): ...
def argwhere(a): ...
def flatnonzero(a): ...
def correlate(a, v, mode: str = 'valid'): ...
def convolve(a, v, mode: str = 'full'): ...
def outer(a, b, out: Incomplete | None = None): ...
def tensordot(a, b, axes: int = 2): ...
def roll(a, shift, axis: Incomplete | None = None): ...
def rollaxis(a, axis, start: int = 0): ...
def moveaxis(a, source, destination): ...
def cross(a, b, axisa: int = -1, axisb: int = -1, axisc: int = -1, axis: Incomplete | None = None): ...

little_endian: Incomplete

def indices(dimensions, dtype=..., sparse: bool = False): ...
def fromfunction(function, shape, *, dtype=..., like: Incomplete | None = None, **kwargs): ...
def isscalar(element): ...
def binary_repr(num, width: Incomplete | None = None): ...
def base_repr(number, base: int = 2, padding: int = 0): ...
def identity(n, dtype: Incomplete | None = None, *, like: Incomplete | None = None): ...
def allclose(a, b, rtol: float = 1e-05, atol: float = 1e-08, equal_nan: bool = False): ...
def isclose(a, b, rtol: float = 1e-05, atol: float = 1e-08, equal_nan: bool = False): ...
def array_equal(a1, a2, equal_nan: bool = False): ...
def array_equiv(a1, a2): ...
def astype(x, dtype, /, *, copy: bool = True, device: Incomplete | None = None): ...
inf = PINF
nan = NAN
False_: Incomplete
True_: Incomplete

# Names in __all__ with no definition:
#   ScalarType
#   absolute
#   add
#   all
#   amax
#   amin
#   any
#   arccos
#   arccosh
#   arcsin
#   arcsinh
#   arctan
#   arctan2
#   arctanh
#   argmax
#   argmin
#   argpartition
#   argsort
#   around
#   array2string
#   array_repr
#   array_str
#   bitwise_and
#   bitwise_count
#   bitwise_or
#   bitwise_xor
#   bool
#   bool_
#   busday_count
#   busday_offset
#   busdaycalendar
#   byte
#   bytes_
#   cbrt
#   cdouble
#   ceil
#   character
#   choose
#   clip
#   clongdouble
#   complex128
#   complex64
#   complexfloating
#   compress
#   conj
#   conjugate
#   copysign
#   cos
#   cosh
#   csingle
#   cumprod
#   cumsum
#   cumulative_prod
#   cumulative_sum
#   datetime64
#   datetime_as_string
#   datetime_data
#   deg2rad
#   degrees
#   diagonal
#   divide
#   divmod
#   double
#   e
#   equal
#   euler_gamma
#   exp
#   exp2
#   expm1
#   fabs
#   flexible
#   float16
#   float32
#   float64
#   float_power
#   floating
#   floor
#   floor_divide
#   fmax
#   fmin
#   fmod
#   format_float_positional
#   format_float_scientific
#   frexp
#   frompyfunc
#   gcd
#   generic
#   get_printoptions
#   getbufsize
#   geterr
#   geterrcall
#   greater
#   greater_equal
#   half
#   heaviside
#   hypot
#   inexact
#   int16
#   int32
#   int64
#   int8
#   int_
#   intc
#   integer
#   intp
#   is_busday
#   isdtype
#   isfinite
#   isinf
#   isnan
#   isnat
#   issubdtype
#   lcm
#   ldexp
#   left_shift
#   less
#   less_equal
#   log
#   log10
#   log1p
#   log2
#   logaddexp
#   logaddexp2
#   logical_and
#   logical_not
#   logical_or
#   logical_xor
#   long
#   longdouble
#   longlong
#   matrix_transpose
#   matvec
#   max
#   maximum
#   mean
#   min
#   minimum
#   mod
#   modf
#   ndim
#   negative
#   nextafter
#   nonzero
#   not_equal
#   number
#   object_
#   partition
#   pi
#   positive
#   power
#   printoptions
#   prod
#   ptp
#   put
#   rad2deg
#   radians
#   ravel
#   reciprocal
#   remainder
#   repeat
#   require
#   reshape
#   resize
#   right_shift
#   rint
#   round
#   searchsorted
#   set_printoptions
#   setbufsize
#   seterr
#   seterrcall
#   shape
#   short
#   sign
#   signbit
#   signedinteger
#   single
#   sinh
#   size
#   sort
#   spacing
#   sqrt
#   square
#   squeeze
#   std
#   str_
#   subtract
#   sum
#   swapaxes
#   take
#   tan
#   tanh
#   timedelta64
#   trace
#   transpose
#   true_divide
#   trunc
#   typecodes
#   ubyte
#   uint
#   uint16
#   uint32
#   uint64
#   uint8
#   uintc
#   uintp
#   ulong
#   ulonglong
#   unsignedinteger
#   ushort
#   var
#   vecmat
#   void
