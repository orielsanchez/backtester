from _typeshed import Incomplete

__all__ = ['FormatError', 'PkgNotFound', 'LibraryInfo', 'VariableSet', 'read_config', 'parse_flags']

class FormatError(OSError):
    msg: Incomplete
    def __init__(self, msg) -> None: ...

class PkgNotFound(OSError):
    msg: Incomplete
    def __init__(self, msg) -> None: ...

def parse_flags(line): ...

class LibraryInfo:
    name: Incomplete
    description: Incomplete
    requires: Incomplete
    version: Incomplete
    vars: Incomplete
    def __init__(self, name, description, version, sections, vars, requires: Incomplete | None = None) -> None: ...
    def sections(self): ...
    def cflags(self, section: str = 'default'): ...
    def libs(self, section: str = 'default'): ...

class VariableSet:
    def __init__(self, d) -> None: ...
    def interpolate(self, value): ...
    def variables(self): ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...

def read_config(pkgname, dirs: Incomplete | None = None): ...
