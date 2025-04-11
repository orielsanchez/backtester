from _typeshed import Incomplete
from collections.abc import Iterable

class TablePlotter:
    cell_width: Incomplete
    cell_height: Incomplete
    font_size: Incomplete
    def __init__(self, cell_width: float = 0.37, cell_height: float = 0.25, font_size: float = 7.5) -> None: ...
    def plot(self, left, right, labels: Iterable[str] = (), vertical: bool = True): ...

def main() -> None: ...
