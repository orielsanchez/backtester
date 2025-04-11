from _typeshed import Incomplete
from pandas._typing import ExcelWriterIfSheetExists as ExcelWriterIfSheetExists, FilePath as FilePath, StorageOptions as StorageOptions, WriteExcelBuffer as WriteExcelBuffer
from pandas.io.excel._base import ExcelWriter as ExcelWriter
from pandas.io.excel._util import combine_kwargs as combine_kwargs, validate_freeze_panes as validate_freeze_panes
from pandas.io.formats.excel import ExcelCell as ExcelCell
from typing import Any

class ODSWriter(ExcelWriter):
    def __init__(self, path: FilePath | WriteExcelBuffer | ExcelWriter, engine: str | None = None, date_format: str | None = None, datetime_format: Incomplete | None = None, mode: str = 'w', storage_options: StorageOptions | None = None, if_sheet_exists: ExcelWriterIfSheetExists | None = None, engine_kwargs: dict[str, Any] | None = None, **kwargs) -> None: ...
    @property
    def book(self): ...
    @property
    def sheets(self) -> dict[str, Any]: ...
