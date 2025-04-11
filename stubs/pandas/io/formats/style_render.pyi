from _typeshed import Incomplete
from collections.abc import Sequence
from pandas import DataFrame as DataFrame, Index as Index, IndexSlice as IndexSlice, MultiIndex as MultiIndex, Series as Series, isna as isna
from pandas._config import get_option as get_option
from pandas._libs import lib as lib
from pandas._typing import Axis as Axis, Level as Level
from pandas.api.types import is_list_like as is_list_like
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.dtypes.common import is_complex as is_complex, is_float as is_float, is_integer as is_integer
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from typing import Any, Callable, DefaultDict, TypedDict

jinja2: Incomplete
BaseFormatter = str | Callable
ExtFormatter = BaseFormatter | dict[Any, BaseFormatter | None]
CSSPair = tuple[str, str | float]
CSSList = list[CSSPair]
CSSProperties = str | CSSList

class CSSDict(TypedDict):
    selector: str
    props: CSSProperties
CSSStyles = list[CSSDict]
Subset = slice | Sequence | Index

class StylerRenderer:
    loader: Incomplete
    env: Incomplete
    template_html: Incomplete
    template_html_table: Incomplete
    template_html_style: Incomplete
    template_latex: Incomplete
    template_string: Incomplete
    data: DataFrame
    index: Index
    columns: Index
    uuid: Incomplete
    uuid_len: Incomplete
    table_styles: Incomplete
    table_attributes: Incomplete
    caption: Incomplete
    cell_ids: Incomplete
    css: Incomplete
    concatenated: list[StylerRenderer]
    hide_index_names: bool
    hide_column_names: bool
    hide_index_: list
    hide_columns_: list
    hidden_rows: Sequence[int]
    hidden_columns: Sequence[int]
    ctx: DefaultDict[tuple[int, int], CSSList]
    ctx_index: DefaultDict[tuple[int, int], CSSList]
    ctx_columns: DefaultDict[tuple[int, int], CSSList]
    cell_context: DefaultDict[tuple[int, int], str]
    tooltips: Tooltips | None
    def __init__(self, data: DataFrame | Series, uuid: str | None = None, uuid_len: int = 5, table_styles: CSSStyles | None = None, table_attributes: str | None = None, caption: str | tuple | list | None = None, cell_ids: bool = True, precision: int | None = None) -> None: ...
    def format(self, formatter: ExtFormatter | None = None, subset: Subset | None = None, na_rep: str | None = None, precision: int | None = None, decimal: str = '.', thousands: str | None = None, escape: str | None = None, hyperlinks: str | None = None) -> StylerRenderer: ...
    def format_index(self, formatter: ExtFormatter | None = None, axis: Axis = 0, level: Level | list[Level] | None = None, na_rep: str | None = None, precision: int | None = None, decimal: str = '.', thousands: str | None = None, escape: str | None = None, hyperlinks: str | None = None) -> StylerRenderer: ...
    def relabel_index(self, labels: Sequence | Index, axis: Axis = 0, level: Level | list[Level] | None = None) -> StylerRenderer: ...

def format_table_styles(styles: CSSStyles) -> CSSStyles: ...
def non_reducing_slice(slice_: Subset): ...
def maybe_convert_css_to_tuples(style: CSSProperties) -> CSSList: ...
def refactor_levels(level: Level | list[Level] | None, obj: Index) -> list[int]: ...

class Tooltips:
    class_name: Incomplete
    class_properties: Incomplete
    tt_data: Incomplete
    table_styles: CSSStyles
    def __init__(self, css_props: CSSProperties = [('visibility', 'hidden'), ('position', 'absolute'), ('z-index', 1), ('background-color', 'black'), ('color', 'white'), ('transform', 'translate(-20px, -20px)')], css_name: str = 'pd-t', tooltips: DataFrame = ...) -> None: ...
