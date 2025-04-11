import scipy.sparse
from collections.abc import Iterable
from pandas._libs import lib as lib
from pandas._typing import IndexLabel as IndexLabel, npt as npt
from pandas.core.algorithms import factorize as factorize
from pandas.core.dtypes.missing import notna as notna
from pandas.core.indexes.api import MultiIndex as MultiIndex
from pandas.core.series import Series as Series

def sparse_series_to_coo(ss: Series, row_levels: Iterable[int] = (0,), column_levels: Iterable[int] = (1,), sort_labels: bool = False) -> tuple[scipy.sparse.coo_matrix, list[IndexLabel], list[IndexLabel]]: ...
def coo_to_sparse_series(A: scipy.sparse.coo_matrix, dense_index: bool = False) -> Series: ...
