from pandas.core.algorithms import unique1d as unique1d
from pandas.core.arrays.categorical import Categorical as Categorical, CategoricalDtype as CategoricalDtype, recode_for_categories as recode_for_categories

def recode_for_groupby(c: Categorical, sort: bool, observed: bool) -> tuple[Categorical, Categorical | None]: ...
