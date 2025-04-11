from _typeshed import Incomplete
from pandas import Index as Index
from pandas._libs import NaT as NaT, lib as lib
from pandas._libs.missing import NA as NA
from pandas._typing import ArrayLike as ArrayLike, AxisInt as AxisInt, DtypeObj as DtypeObj, Manager2D as Manager2D, Shape as Shape
from pandas.core.construction import ensure_wrapped_if_datetimelike as ensure_wrapped_if_datetimelike
from pandas.core.dtypes.cast import ensure_dtype_can_hold_na as ensure_dtype_can_hold_na, find_common_type as find_common_type
from pandas.core.dtypes.common import is_1d_only_ea_dtype as is_1d_only_ea_dtype, is_scalar as is_scalar, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.concat import concat_compat as concat_compat
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype, SparseDtype as SparseDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype as is_valid_na_for_dtype, isna as isna, isna_all as isna_all
from pandas.core.internals.array_manager import ArrayManager as ArrayManager
from pandas.core.internals.blocks import Block as Block, BlockPlacement as BlockPlacement, ensure_block_shape as ensure_block_shape, new_block_2d as new_block_2d
from pandas.core.internals.managers import BlockManager as BlockManager, make_na_array as make_na_array
from pandas.util._decorators import cache_readonly as cache_readonly
from pandas.util._exceptions import find_stack_level as find_stack_level

def concatenate_managers(mgrs_indexers, axes: list[Index], concat_axis: AxisInt, copy: bool) -> Manager2D: ...

class JoinUnit:
    block: Incomplete
    def __init__(self, block: Block) -> None: ...
    def is_na(self) -> bool: ...
    def is_na_after_size_and_isna_all_deprecation(self) -> bool: ...
    def get_reindexed_values(self, empty_dtype: DtypeObj, upcasted_na) -> ArrayLike: ...
