from _typeshed import Incomplete
from collections.abc import Hashable, Iterable, Mapping
from pandas import DataFrame as DataFrame, Series as Series
from pandas._config import using_copy_on_write as using_copy_on_write
from pandas._typing import Axis as Axis, AxisInt as AxisInt, HashableT as HashableT
from pandas.core.arrays.categorical import factorize_from_iterable as factorize_from_iterable, factorize_from_iterables as factorize_from_iterables
from pandas.core.dtypes.common import is_bool as is_bool, is_iterator as is_iterator
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, all_indexes_same as all_indexes_same, default_index as default_index, ensure_index as ensure_index, get_objs_combined_axis as get_objs_combined_axis, get_unanimous_names as get_unanimous_names
from pandas.core.internals import concatenate_managers as concatenate_managers
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Literal, overload

@overload
def concat(objs: Iterable[DataFrame] | Mapping[HashableT, DataFrame], *, axis: Literal[0, 'index'] = ..., join: str = ..., ignore_index: bool = ..., keys: Iterable[Hashable] | None = ..., levels=..., names: list[HashableT] | None = ..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame: ...
@overload
def concat(objs: Iterable[Series] | Mapping[HashableT, Series], *, axis: Literal[0, 'index'] = ..., join: str = ..., ignore_index: bool = ..., keys: Iterable[Hashable] | None = ..., levels=..., names: list[HashableT] | None = ..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> Series: ...
@overload
def concat(objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame], *, axis: Literal[0, 'index'] = ..., join: str = ..., ignore_index: bool = ..., keys: Iterable[Hashable] | None = ..., levels=..., names: list[HashableT] | None = ..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame | Series: ...
@overload
def concat(objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame], *, axis: Literal[1, 'columns'], join: str = ..., ignore_index: bool = ..., keys: Iterable[Hashable] | None = ..., levels=..., names: list[HashableT] | None = ..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame: ...
@overload
def concat(objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame], *, axis: Axis = ..., join: str = ..., ignore_index: bool = ..., keys: Iterable[Hashable] | None = ..., levels=..., names: list[HashableT] | None = ..., verify_integrity: bool = ..., sort: bool = ..., copy: bool | None = ...) -> DataFrame | Series: ...

class _Concatenator:
    sort: bool
    intersect: bool
    ignore_index: Incomplete
    verify_integrity: Incomplete
    copy: Incomplete
    objs: Incomplete
    bm_axis: Incomplete
    axis: Incomplete
    keys: Incomplete
    names: Incomplete
    levels: Incomplete
    def __init__(self, objs: Iterable[Series | DataFrame] | Mapping[HashableT, Series | DataFrame], axis: Axis = 0, join: str = 'outer', keys: Iterable[Hashable] | None = None, levels: Incomplete | None = None, names: list[HashableT] | None = None, ignore_index: bool = False, verify_integrity: bool = False, copy: bool = True, sort: bool = False) -> None: ...
    def get_result(self): ...
    def new_axes(self) -> list[Index]: ...
