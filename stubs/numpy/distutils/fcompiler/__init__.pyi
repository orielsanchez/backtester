from _typeshed import Incomplete
from numpy.distutils.ccompiler import CCompiler

__all__ = ['FCompiler', 'new_fcompiler', 'show_fcompilers', 'dummy_fortran_file']

__metaclass__ = type

class CompilerNotFound(Exception): ...

class FCompiler(CCompiler):
    distutils_vars: Incomplete
    command_vars: Incomplete
    flag_vars: Incomplete
    language_map: Incomplete
    language_order: Incomplete
    compiler_type: Incomplete
    compiler_aliases: Incomplete
    version_pattern: Incomplete
    possible_executables: Incomplete
    executables: Incomplete
    suggested_f90_compiler: Incomplete
    compile_switch: str
    object_switch: str
    library_switch: str
    module_dir_switch: Incomplete
    module_include_switch: str
    pic_flags: Incomplete
    src_extensions: Incomplete
    obj_extension: str
    shared_lib_extension: Incomplete
    static_lib_extension: str
    static_lib_format: str
    shared_lib_format: str
    exe_extension: str
    c_compiler: Incomplete
    extra_f77_compile_args: Incomplete
    extra_f90_compile_args: Incomplete
    def __init__(self, *args, **kw) -> None: ...
    def __copy__(self): ...
    def copy(self): ...
    version_cmd: Incomplete
    compiler_f77: Incomplete
    compiler_f90: Incomplete
    compiler_fix: Incomplete
    linker_so: Incomplete
    linker_exe: Incomplete
    archiver: Incomplete
    ranlib: Incomplete
    def set_executable(self, key, value) -> None: ...
    def set_commands(self, **kw) -> None: ...
    def set_command(self, key, value) -> None: ...
    def find_executables(self): ...
    def update_executables(self) -> None: ...
    def get_flags(self): ...
    def get_flags_f77(self): ...
    def get_flags_f90(self): ...
    def get_flags_free(self): ...
    def get_flags_fix(self): ...
    def get_flags_linker_so(self): ...
    def get_flags_linker_exe(self): ...
    def get_flags_ar(self): ...
    def get_flags_opt(self): ...
    def get_flags_arch(self): ...
    def get_flags_debug(self): ...
    get_flags_opt_f77 = get_flags_opt
    get_flags_opt_f90 = get_flags_opt
    get_flags_arch_f77 = get_flags_arch
    get_flags_arch_f90 = get_flags_arch
    get_flags_debug_f77 = get_flags_debug
    get_flags_debug_f90 = get_flags_debug
    def get_libraries(self): ...
    def get_library_dirs(self): ...
    def get_version(self, force: bool = False, ok_status=[0]): ...
    def customize(self, dist: Incomplete | None = None) -> None: ...
    def dump_properties(self) -> None: ...
    def module_options(self, module_dirs, module_build_dir): ...
    def library_option(self, lib): ...
    def library_dir_option(self, dir): ...
    def link(self, target_desc, objects, output_filename, output_dir: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, export_symbols: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, build_temp: Incomplete | None = None, target_lang: Incomplete | None = None) -> None: ...
    def can_ccompiler_link(self, ccompiler): ...
    def wrap_unlinkable_objects(self, objects, output_dir, extra_dll_dir) -> None: ...

def new_fcompiler(plat: Incomplete | None = None, compiler: Incomplete | None = None, verbose: int = 0, dry_run: int = 0, force: int = 0, requiref90: bool = False, c_compiler: Incomplete | None = None): ...
def show_fcompilers(dist: Incomplete | None = None) -> None: ...
def dummy_fortran_file(): ...
