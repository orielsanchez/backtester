from _typeshed import Incomplete
from collections.abc import Hashable, Iterable, Mapping, Sequence
from pandas import DataFrame as DataFrame, ExcelWriter as ExcelWriter, Index as Index, MultiIndex as MultiIndex, PeriodIndex as PeriodIndex
from pandas._libs.lib import is_list_like as is_list_like
from pandas._typing import FilePath as FilePath, IndexLabel as IndexLabel, StorageOptions as StorageOptions, WriteExcelBuffer as WriteExcelBuffer
from pandas.core.dtypes import missing as missing
from pandas.core.dtypes.common import is_float as is_float, is_scalar as is_scalar
from pandas.io.formats._color_data import CSS4_COLORS as CSS4_COLORS
from pandas.io.formats.css import CSSResolver as CSSResolver, CSSWarning as CSSWarning
from pandas.io.formats.format import get_level_lengths as get_level_lengths
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.util._decorators import doc as doc
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Any, Callable

class ExcelCell:
    __fields__: Incomplete
    row: Incomplete
    col: Incomplete
    val: Incomplete
    style: Incomplete
    mergestart: Incomplete
    mergeend: Incomplete
    def __init__(self, row: int, col: int, val, style: Incomplete | None = None, mergestart: int | None = None, mergeend: int | None = None) -> None: ...

class CssExcelCell(ExcelCell):
    def __init__(self, row: int, col: int, val, style: dict | None, css_styles: dict[tuple[int, int], list[tuple[str, Any]]] | None, css_row: int, css_col: int, css_converter: Callable | None, **kwargs) -> None: ...

class CSSToExcelConverter:
    NAMED_COLORS = CSS4_COLORS
    VERTICAL_MAP: Incomplete
    BOLD_MAP: Incomplete
    ITALIC_MAP: Incomplete
    FAMILY_MAP: Incomplete
    BORDER_STYLE_MAP: Incomplete
    inherited: dict[str, str] | None
    def __init__(self, inherited: str | None = None) -> None: ...
    compute_css: Incomplete
    def __call__(self, declarations: str | frozenset[tuple[str, str]]) -> dict[str, dict[str, str]]: ...
    def build_xlstyle(self, props: Mapping[str, str]) -> dict[str, dict[str, str]]: ...
    def build_alignment(self, props: Mapping[str, str]) -> dict[str, bool | str | None]: ...
    def build_border(self, props: Mapping[str, str]) -> dict[str, dict[str, str | None]]: ...
    def build_fill(self, props: Mapping[str, str]): ...
    def build_number_format(self, props: Mapping[str, str]) -> dict[str, str | None]: ...
    def build_font(self, props: Mapping[str, str]) -> dict[str, bool | float | str | None]: ...
    def color_to_excel(self, val: str | None) -> str | None: ...

class ExcelFormatter:
    max_rows: Incomplete
    max_cols: Incomplete
    rowcounter: int
    na_rep: Incomplete
    styler: Incomplete
    style_converter: Callable | None
    df: Incomplete
    columns: Incomplete
    float_format: Incomplete
    index: Incomplete
    index_label: Incomplete
    header: Incomplete
    merge_cells: Incomplete
    inf_rep: Incomplete
    def __init__(self, df, na_rep: str = '', float_format: str | None = None, cols: Sequence[Hashable] | None = None, header: Sequence[Hashable] | bool = True, index: bool = True, index_label: IndexLabel | None = None, merge_cells: bool = False, inf_rep: str = 'inf', style_converter: Callable | None = None) -> None: ...
    @property
    def header_style(self) -> dict[str, dict[str, str | bool]]: ...
    def get_formatted_cells(self) -> Iterable[ExcelCell]: ...
    def write(self, writer: FilePath | WriteExcelBuffer | ExcelWriter, sheet_name: str = 'Sheet1', startrow: int = 0, startcol: int = 0, freeze_panes: tuple[int, int] | None = None, engine: str | None = None, storage_options: StorageOptions | None = None, engine_kwargs: dict | None = None) -> None: ...
