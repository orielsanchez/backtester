from pandas._typing import ArrayLike as ArrayLike, npt as npt
from pandas.core.arrays import IntervalArray as IntervalArray
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray as NDArrayBackedExtensionArray
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame
from pandas.core.indexes.base import Index as Index
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Callable

def inherit_names(names: list[str], delegate: type, cache: bool = False, wrap: bool = False) -> Callable[[type[_ExtensionIndexT]], type[_ExtensionIndexT]]: ...

class ExtensionIndex(Index): ...
class NDArrayBackedExtensionIndex(ExtensionIndex): ...
