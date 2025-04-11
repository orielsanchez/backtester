from google.auth.credentials import Credentials as Credentials
from pandas import DataFrame as DataFrame
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Any

def read_gbq(query: str, project_id: str | None = None, index_col: str | None = None, col_order: list[str] | None = None, reauth: bool = False, auth_local_webserver: bool = True, dialect: str | None = None, location: str | None = None, configuration: dict[str, Any] | None = None, credentials: Credentials | None = None, use_bqstorage_api: bool | None = None, max_results: int | None = None, progress_bar_type: str | None = None) -> DataFrame: ...
def to_gbq(dataframe: DataFrame, destination_table: str, project_id: str | None = None, chunksize: int | None = None, reauth: bool = False, if_exists: str = 'fail', auth_local_webserver: bool = True, table_schema: list[dict[str, str]] | None = None, location: str | None = None, progress_bar: bool = True, credentials: Credentials | None = None) -> None: ...
