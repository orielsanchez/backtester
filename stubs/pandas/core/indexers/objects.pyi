import numpy as np
from _typeshed import Incomplete
from pandas._libs.tslibs import BaseOffset as BaseOffset
from pandas._libs.window.indexers import calculate_variable_window_bounds as calculate_variable_window_bounds
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.tseries.offsets import Nano as Nano
from pandas.util._decorators import Appender as Appender

get_window_bounds_doc: str

class BaseIndexer:
    index_array: Incomplete
    window_size: Incomplete
    def __init__(self, index_array: np.ndarray | None = None, window_size: int = 0, **kwargs) -> None: ...
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class FixedWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class VariableWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class VariableOffsetWindowIndexer(BaseIndexer):
    index: Incomplete
    offset: Incomplete
    def __init__(self, index_array: np.ndarray | None = None, window_size: int = 0, index: DatetimeIndex | None = None, offset: BaseOffset | None = None, **kwargs) -> None: ...
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class ExpandingIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class FixedForwardWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class GroupbyIndexer(BaseIndexer):
    groupby_indices: Incomplete
    window_indexer: Incomplete
    indexer_kwargs: Incomplete
    def __init__(self, index_array: np.ndarray | None = None, window_size: int | BaseIndexer = 0, groupby_indices: dict | None = None, window_indexer: type[BaseIndexer] = ..., indexer_kwargs: dict | None = None, **kwargs) -> None: ...
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class ExponentialMovingWindowIndexer(BaseIndexer):
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...
