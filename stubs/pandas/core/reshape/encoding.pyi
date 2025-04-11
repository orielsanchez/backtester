from _typeshed import Incomplete
from collections.abc import Hashable, Iterable
from pandas._libs.sparse import IntIndex as IntIndex
from pandas._typing import NpDtype as NpDtype
from pandas.core.arrays import SparseArray as SparseArray
from pandas.core.arrays.categorical import factorize_from_iterable as factorize_from_iterable
from pandas.core.arrays.string_ import StringDtype as StringDtype
from pandas.core.dtypes.common import is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype as ArrowDtype, CategoricalDtype as CategoricalDtype
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.api import Index as Index, default_index as default_index
from pandas.core.series import Series as Series

def get_dummies(data, prefix: Incomplete | None = None, prefix_sep: str | Iterable[str] | dict[str, str] = '_', dummy_na: bool = False, columns: Incomplete | None = None, sparse: bool = False, drop_first: bool = False, dtype: NpDtype | None = None) -> DataFrame: ...
def from_dummies(data: DataFrame, sep: None | str = None, default_category: None | Hashable | dict[str, Hashable] = None) -> DataFrame: ...
