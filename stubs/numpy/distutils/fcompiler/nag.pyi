from _typeshed import Incomplete
from numpy.distutils.fcompiler import FCompiler as FCompiler

compilers: Incomplete

class BaseNAGFCompiler(FCompiler):
    version_pattern: str
    def version_match(self, version_string): ...
    def get_flags_linker_so(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...

class NAGFCompiler(BaseNAGFCompiler):
    compiler_type: str
    description: str
    executables: Incomplete
    def get_flags_linker_so(self): ...
    def get_flags_arch(self): ...
    def get_flags_debug(self): ...

class NAGFORCompiler(BaseNAGFCompiler):
    compiler_type: str
    description: str
    executables: Incomplete
    def get_flags_linker_so(self): ...
    def get_flags_debug(self): ...
