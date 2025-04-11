import numpy as np
from pandas._typing import Scalar as Scalar
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.util.numba_ import NumbaUtilError as NumbaUtilError, jit_user_function as jit_user_function
from typing import Any, Callable

def validate_udf(func: Callable) -> None: ...
def generate_numba_agg_func(func: Callable[..., Scalar], nopython: bool, nogil: bool, parallel: bool) -> Callable[[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, Any], np.ndarray]: ...
def generate_numba_transform_func(func: Callable[..., np.ndarray], nopython: bool, nogil: bool, parallel: bool) -> Callable[[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, Any], np.ndarray]: ...
