import abc
import numpy as np
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Hashable, Sequence
from pandas import DataFrame as DataFrame, Series as Series
from pandas._libs.tslibs import Timestamp as Timestamp
from pandas._typing import DtypeObj as DtypeObj, NDFrameT as NDFrameT, npt as npt
from pandas.core.arrays.floating import Float64Dtype as Float64Dtype
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_numeric_dtype as is_numeric_dtype
from pandas.core.dtypes.dtypes import ArrowDtype as ArrowDtype, DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype
from pandas.core.reshape.concat import concat as concat
from pandas.io.formats.format import format_percentiles as format_percentiles
from pandas.util._validators import validate_percentile as validate_percentile
from typing import Callable

def describe_ndframe(*, obj: NDFrameT, include: str | Sequence[str] | None, exclude: str | Sequence[str] | None, percentiles: Sequence[float] | np.ndarray | None) -> NDFrameT: ...

class NDFrameDescriberAbstract(ABC, metaclass=abc.ABCMeta):
    obj: Incomplete
    def __init__(self, obj: DataFrame | Series) -> None: ...
    @abstractmethod
    def describe(self, percentiles: Sequence[float] | np.ndarray) -> DataFrame | Series: ...

class SeriesDescriber(NDFrameDescriberAbstract):
    obj: Series
    def describe(self, percentiles: Sequence[float] | np.ndarray) -> Series: ...

class DataFrameDescriber(NDFrameDescriberAbstract):
    obj: DataFrame
    include: Incomplete
    exclude: Incomplete
    def __init__(self, obj: DataFrame, *, include: str | Sequence[str] | None, exclude: str | Sequence[str] | None) -> None: ...
    def describe(self, percentiles: Sequence[float] | np.ndarray) -> DataFrame: ...

def reorder_columns(ldesc: Sequence[Series]) -> list[Hashable]: ...
def describe_numeric_1d(series: Series, percentiles: Sequence[float]) -> Series: ...
def describe_categorical_1d(data: Series, percentiles_ignored: Sequence[float]) -> Series: ...
def describe_timestamp_as_categorical_1d(data: Series, percentiles_ignored: Sequence[float]) -> Series: ...
def describe_timestamp_1d(data: Series, percentiles: Sequence[float]) -> Series: ...
def select_describe_func(data: Series) -> Callable: ...
