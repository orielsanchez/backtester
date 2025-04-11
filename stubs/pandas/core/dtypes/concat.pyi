from collections.abc import Sequence
from pandas._libs import lib as lib
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj
from pandas.core.arrays import Categorical as Categorical, ExtensionArray as ExtensionArray
from pandas.core.dtypes.astype import astype_array as astype_array
from pandas.core.dtypes.cast import common_dtype_categorical_compat as common_dtype_categorical_compat, find_common_type as find_common_type, np_find_common_type as np_find_common_type
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.dtypes.generic import ABCCategoricalIndex as ABCCategoricalIndex, ABCSeries as ABCSeries
from pandas.util._exceptions import find_stack_level as find_stack_level

def concat_compat(to_concat: Sequence[ArrayLike], axis: AxisInt = 0, ea_compat_axis: bool = False) -> ArrayLike: ...
def union_categoricals(to_union, sort_categories: bool = False, ignore_order: bool = False) -> Categorical: ...
