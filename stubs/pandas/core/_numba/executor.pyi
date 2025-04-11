import numpy as np
from pandas._typing import Scalar as Scalar
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from typing import Any, Callable

def generate_apply_looper(func, nopython: bool = True, nogil: bool = True, parallel: bool = False): ...
def make_looper(func, result_dtype, is_grouped_kernel, nopython, nogil, parallel): ...

default_dtype_mapping: dict[np.dtype, Any]
float_dtype_mapping: dict[np.dtype, Any]
identity_dtype_mapping: dict[np.dtype, Any]

def generate_shared_aggregator(func: Callable[..., Scalar], dtype_mapping: dict[np.dtype, np.dtype], is_grouped_kernel: bool, nopython: bool, nogil: bool, parallel: bool): ...
