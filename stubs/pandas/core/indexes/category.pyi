import numpy as np
from _typeshed import Incomplete
from collections.abc import Hashable
from pandas._typing import Dtype as Dtype, DtypeObj as DtypeObj, Self as Self, npt as npt
from pandas.core.arrays.categorical import Categorical as Categorical, contains as contains
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.common import is_scalar as is_scalar
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna
from pandas.core.indexes.base import Index as Index, maybe_extract_name as maybe_extract_name
from pandas.core.indexes.extension import NDArrayBackedExtensionIndex as NDArrayBackedExtensionIndex, inherit_names as inherit_names
from pandas.util._decorators import cache_readonly as cache_readonly, doc as doc
from typing import Any, Literal

class CategoricalIndex(NDArrayBackedExtensionIndex):
    codes: np.ndarray
    categories: Index
    ordered: bool | None
    def __new__(cls, data: Incomplete | None = None, categories: Incomplete | None = None, ordered: Incomplete | None = None, dtype: Dtype | None = None, copy: bool = False, name: Hashable | None = None) -> Self: ...
    def equals(self, other: object) -> bool: ...
    @property
    def inferred_type(self) -> str: ...
    def __contains__(self, key: Any) -> bool: ...
    def reindex(self, target, method: Incomplete | None = None, level: Incomplete | None = None, limit: int | None = None, tolerance: Incomplete | None = None) -> tuple[Index, npt.NDArray[np.intp] | None]: ...
    def map(self, mapper, na_action: Literal['ignore'] | None = None): ...
