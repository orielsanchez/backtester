import numpy as np
from pandas._libs import lib as lib
from pandas._typing import AxisInt as AxisInt
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.generic import NDFrame as NDFrame

def preprocess_weights(obj: NDFrame, weights, axis: AxisInt) -> np.ndarray: ...
def process_sampling_size(n: int | None, frac: float | None, replace: bool) -> int | None: ...
def sample(obj_len: int, size: int, replace: bool, weights: np.ndarray | None, random_state: np.random.RandomState | np.random.Generator) -> np.ndarray: ...
