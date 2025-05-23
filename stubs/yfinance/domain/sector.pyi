import pandas as _pd
from .. import utils as utils
from ..const import SECTOR_INDUSTY_MAPPING as SECTOR_INDUSTY_MAPPING
from ..utils import dynamic_docstring as dynamic_docstring, generate_list_table_from_dict as generate_list_table_from_dict
from .domain import Domain as Domain
from _typeshed import Incomplete

class Sector(Domain):
    def __init__(self, key, session: Incomplete | None = None, proxy: Incomplete | None = None) -> None: ...
    @property
    def top_etfs(self) -> dict[str, str]: ...
    @property
    def top_mutual_funds(self) -> dict[str, str]: ...
    @property
    def industries(self) -> _pd.DataFrame: ...
