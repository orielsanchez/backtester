from _typeshed import Incomplete
from pandas._libs.internals import BlockPlacement as BlockPlacement
from pandas._typing import Dtype as Dtype
from pandas.core.arrays import DatetimeArray as DatetimeArray
from pandas.core.construction import extract_array as extract_array
from pandas.core.dtypes.common import pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, PeriodDtype as PeriodDtype
from pandas.core.internals.blocks import Block as Block, check_ndim as check_ndim, ensure_block_shape as ensure_block_shape, extract_pandas_array as extract_pandas_array, get_block_type as get_block_type, maybe_coerce_values as maybe_coerce_values

def make_block(values, placement, klass: Incomplete | None = None, ndim: Incomplete | None = None, dtype: Dtype | None = None) -> Block: ...
def maybe_infer_ndim(values, placement: BlockPlacement, ndim: int | None) -> int: ...
def __getattr__(name: str): ...
