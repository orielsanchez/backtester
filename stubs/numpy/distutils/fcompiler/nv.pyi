from _typeshed import Incomplete
from numpy.distutils.fcompiler import FCompiler as FCompiler

compilers: Incomplete

class NVHPCFCompiler(FCompiler):
    compiler_type: str
    description: str
    version_pattern: str
    executables: Incomplete
    pic_flags: Incomplete
    module_dir_switch: str
    module_include_switch: str
    def get_flags(self): ...
    def get_flags_opt(self): ...
    def get_flags_debug(self): ...
    def get_flags_linker_so(self): ...
    def runtime_library_dir_option(self, dir): ...
