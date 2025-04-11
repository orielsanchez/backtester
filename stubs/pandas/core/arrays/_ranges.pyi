import numpy as np
from pandas._libs.lib import i8max as i8max
from pandas._libs.tslibs import BaseOffset as BaseOffset, OutOfBoundsDatetime as OutOfBoundsDatetime, Timedelta as Timedelta, Timestamp as Timestamp, iNaT as iNaT
from pandas._typing import npt as npt

def generate_regular_range(start: Timestamp | Timedelta | None, end: Timestamp | Timedelta | None, periods: int | None, freq: BaseOffset, unit: str = 'ns') -> npt.NDArray[np.intp]: ...
