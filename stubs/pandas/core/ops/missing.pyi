import numpy as np
from pandas.core import roperator as roperator

def mask_zero_div_zero(x, y, result: np.ndarray) -> np.ndarray: ...
def dispatch_fill_zeros(op, left, right, result): ...
