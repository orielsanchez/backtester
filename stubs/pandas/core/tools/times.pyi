from pandas._libs.lib import is_list_like as is_list_like
from pandas._typing import DateTimeErrorChoices as DateTimeErrorChoices
from pandas.core.dtypes.generic import ABCIndex as ABCIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import notna as notna
from pandas.util._exceptions import find_stack_level as find_stack_level

def to_time(arg, format: str | None = None, infer_time_format: bool = False, errors: DateTimeErrorChoices = 'raise'): ...
