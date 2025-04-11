from _typeshed import Incomplete
from collections.abc import Hashable
from pandas import DataFrame as DataFrame
from pandas._libs import lib as lib
from pandas._typing import AggFuncType as AggFuncType, AggFuncTypeBase as AggFuncTypeBase, AggFuncTypeDict as AggFuncTypeDict, IndexLabel as IndexLabel
from pandas.core.dtypes.cast import maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import is_list_like as is_list_like, is_nested_list_like as is_nested_list_like, is_scalar as is_scalar
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.groupby import Grouper as Grouper
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, get_objs_combined_axis as get_objs_combined_axis
from pandas.core.reshape.concat import concat as concat
from pandas.core.reshape.util import cartesian_product as cartesian_product
from pandas.core.series import Series as Series
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Literal

def pivot_table(data: DataFrame, values: Incomplete | None = None, index: Incomplete | None = None, columns: Incomplete | None = None, aggfunc: AggFuncType = 'mean', fill_value: Incomplete | None = None, margins: bool = False, dropna: bool = True, margins_name: Hashable = 'All', observed: bool | lib.NoDefault = ..., sort: bool = True) -> DataFrame: ...
def pivot(data: DataFrame, *, columns: IndexLabel, index: IndexLabel | lib.NoDefault = ..., values: IndexLabel | lib.NoDefault = ...) -> DataFrame: ...
def crosstab(index, columns, values: Incomplete | None = None, rownames: Incomplete | None = None, colnames: Incomplete | None = None, aggfunc: Incomplete | None = None, margins: bool = False, margins_name: Hashable = 'All', dropna: bool = True, normalize: bool | Literal[0, 1, 'all', 'index', 'columns'] = False) -> DataFrame: ...
