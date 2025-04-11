from ._type_aliases import sctypeDict
from .multiarray import busday_count as busday_count, busday_offset as busday_offset, busdaycalendar as busdaycalendar, datetime_as_string as datetime_as_string, datetime_data as datetime_data, is_busday as is_busday
from _typeshed import Incomplete
from builtins import bool as bool

__all__ = ['ScalarType', 'typecodes', 'issubdtype', 'datetime_data', 'datetime_as_string', 'busday_offset', 'busday_count', 'is_busday', 'busdaycalendar', 'isdtype', 'character', 'integer', 'generic', 'inexact', 'flexible', 'number', 'floating', 'signedinteger', 'unsignedinteger', 'complexfloating', 'bool', 'float16', 'float32', 'float64', 'longdouble', 'complex64', 'complex128', 'clongdouble', 'bytes_', 'str_', 'void', 'object_', 'datetime64', 'timedelta64', 'int8', 'byte', 'uint8', 'ubyte', 'int16', 'short', 'uint16', 'ushort', 'int32', 'intc', 'uint32', 'uintc', 'int64', 'long', 'uint64', 'ulong', 'longlong', 'ulonglong', 'intp', 'uintp', 'double', 'cdouble', 'single', 'csingle', 'half', 'bool_', 'int_', 'uint']

generic: Incomplete

class _PreprocessDTypeError(Exception): ...

def isdtype(dtype, kind): ...
def issubdtype(arg1, arg2): ...

ScalarType: Incomplete
typecodes: Incomplete
typeDict = sctypeDict

# Names in __all__ with no definition:
#   bool_
#   byte
#   bytes_
#   cdouble
#   character
#   clongdouble
#   complex128
#   complex64
#   complexfloating
#   csingle
#   datetime64
#   double
#   flexible
#   float16
#   float32
#   float64
#   floating
#   half
#   inexact
#   int16
#   int32
#   int64
#   int8
#   int_
#   intc
#   integer
#   intp
#   long
#   longdouble
#   longlong
#   number
#   object_
#   short
#   signedinteger
#   single
#   str_
#   timedelta64
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
#   void
