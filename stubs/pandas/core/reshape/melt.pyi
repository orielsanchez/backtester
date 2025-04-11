from _typeshed import Incomplete
from collections.abc import Hashable
from pandas import DataFrame as DataFrame
from pandas._typing import AnyArrayLike as AnyArrayLike
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.missing import notna as notna
from pandas.core.indexes.api import MultiIndex as MultiIndex
from pandas.core.reshape.concat import concat as concat
from pandas.core.reshape.util import tile_compat as tile_compat
from pandas.core.tools.numeric import to_numeric as to_numeric
from pandas.util._decorators import Appender as Appender

def ensure_list_vars(arg_vars, variable: str, columns) -> list: ...
def melt(frame: DataFrame, id_vars: Incomplete | None = None, value_vars: Incomplete | None = None, var_name: Incomplete | None = None, value_name: Hashable = 'value', col_level: Incomplete | None = None, ignore_index: bool = True) -> DataFrame: ...
def lreshape(data: DataFrame, groups: dict, dropna: bool = True) -> DataFrame: ...
def wide_to_long(df: DataFrame, stubnames, i, j, sep: str = '', suffix: str = '\\d+') -> DataFrame: ...
