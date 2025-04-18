from numpy.testing import assert_ as assert_, assert_allclose as assert_allclose, assert_array_almost_equal_nulp as assert_array_almost_equal_nulp, assert_raises as assert_raises
from unittest import TestCase as TestCase

__all__ = ['almost', 'approx', 'assert_almost_equal', 'assert_array_almost_equal', 'assert_array_approx_equal', 'assert_array_compare', 'assert_array_equal', 'assert_array_less', 'assert_close', 'assert_equal', 'assert_equal_records', 'assert_mask_equal', 'assert_not_equal', 'fail_if_array_equal', 'TestCase', 'assert_', 'assert_allclose', 'assert_array_almost_equal_nulp', 'assert_raises']

def approx(a, b, fill_value: bool = True, rtol: float = 1e-05, atol: float = 1e-08): ...
def almost(a, b, decimal: int = 6, fill_value: bool = True): ...
def assert_equal_records(a, b) -> None: ...
def assert_equal(actual, desired, err_msg: str = ''): ...
assert_not_equal = fail_if_equal

def assert_almost_equal(actual, desired, decimal: int = 7, err_msg: str = '', verbose: bool = True): ...
assert_close = assert_almost_equal

def assert_array_compare(comparison, x, y, err_msg: str = '', verbose: bool = True, header: str = '', fill_value: bool = True): ...
def assert_array_equal(x, y, err_msg: str = '', verbose: bool = True) -> None: ...
def fail_if_array_equal(x, y, err_msg: str = '', verbose: bool = True): ...
def assert_array_approx_equal(x, y, decimal: int = 6, err_msg: str = '', verbose: bool = True): ...
def assert_array_almost_equal(x, y, decimal: int = 6, err_msg: str = '', verbose: bool = True): ...
def assert_array_less(x, y, err_msg: str = '', verbose: bool = True) -> None: ...
def assert_mask_equal(m1, m2, err_msg: str = '') -> None: ...
