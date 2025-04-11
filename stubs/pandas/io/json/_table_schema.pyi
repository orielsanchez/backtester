from pandas import DataFrame as DataFrame, Series as Series
from pandas._libs import lib as lib
from pandas._libs.json import ujson_loads as ujson_loads
from pandas._libs.tslibs import timezones as timezones
from pandas._libs.tslibs.dtypes import freq_to_period_freqstr as freq_to_period_freqstr
from pandas._typing import DtypeObj as DtypeObj, JSONSerializable as JSONSerializable
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_integer_dtype as is_integer_dtype, is_numeric_dtype as is_numeric_dtype, is_string_dtype as is_string_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype, DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype, PeriodDtype as PeriodDtype
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.tseries.frequencies import to_offset as to_offset
from pandas.util._exceptions import find_stack_level as find_stack_level

TABLE_SCHEMA_VERSION: str

def as_json_table_type(x: DtypeObj) -> str: ...
def set_default_names(data): ...
def convert_pandas_type_to_json_field(arr) -> dict[str, JSONSerializable]: ...
def convert_json_field_to_pandas_type(field) -> str | CategoricalDtype: ...
def build_table_schema(data: DataFrame | Series, index: bool = True, primary_key: bool | None = None, version: bool = True) -> dict[str, JSONSerializable]: ...
def parse_table_schema(json, precise_float: bool) -> DataFrame: ...
