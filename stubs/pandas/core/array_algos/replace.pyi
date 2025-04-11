import numpy as np
import re
from pandas._typing import ArrayLike as ArrayLike, Scalar as Scalar, npt as npt
from pandas.core.dtypes.common import is_bool as is_bool, is_re as is_re, is_re_compilable as is_re_compilable
from pandas.core.dtypes.missing import isna as isna
from re import Pattern
from typing import Any

def should_use_regex(regex: bool, to_replace: Any) -> bool: ...
def compare_or_regex_search(a: ArrayLike, b: Scalar | Pattern, regex: bool, mask: npt.NDArray[np.bool_]) -> ArrayLike: ...
def replace_regex(values: ArrayLike, rx: re.Pattern, value, mask: npt.NDArray[np.bool_] | None) -> None: ...
