from pandas._libs import lib as lib
from pandas._typing import DateTimeErrorChoices as DateTimeErrorChoices, DtypeBackend as DtypeBackend, npt as npt
from pandas.core.arrays import BaseMaskedArray as BaseMaskedArray
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.dtypes.cast import maybe_downcast_numeric as maybe_downcast_numeric
from pandas.core.dtypes.common import ensure_object as ensure_object, is_bool_dtype as is_bool_dtype, is_decimal as is_decimal, is_integer_dtype as is_integer_dtype, is_number as is_number, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import ArrowDtype as ArrowDtype
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.util._exceptions import find_stack_level as find_stack_level
from pandas.util._validators import check_dtype_backend as check_dtype_backend
from typing import Literal

def to_numeric(arg, errors: DateTimeErrorChoices = 'raise', downcast: Literal['integer', 'signed', 'unsigned', 'float'] | None = None, dtype_backend: DtypeBackend | lib.NoDefault = ...): ...
