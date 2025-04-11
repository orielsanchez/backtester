from _typeshed import Incomplete
from collections.abc import Generator, Iterable, Iterator
from pandas.errors import CSSWarning as CSSWarning
from pandas.util._exceptions import find_stack_level as find_stack_level

class CSSResolver:
    UNIT_RATIOS: Incomplete
    FONT_SIZE_RATIOS: Incomplete
    MARGIN_RATIOS: Incomplete
    BORDER_WIDTH_RATIOS: Incomplete
    BORDER_STYLES: Incomplete
    SIDE_SHORTHANDS: Incomplete
    SIDES: Incomplete
    CSS_EXPANSIONS: Incomplete
    def __call__(self, declarations: str | Iterable[tuple[str, str]], inherited: dict[str, str] | None = None) -> dict[str, str]: ...
    def size_to_pt(self, in_val, em_pt: Incomplete | None = None, conversions=...) -> str: ...
    def atomize(self, declarations: Iterable) -> Generator[tuple[str, str], None, None]: ...
    def parse(self, declarations_str: str) -> Iterator[tuple[str, str]]: ...
