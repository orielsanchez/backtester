from _typeshed import Incomplete
from distutils.extension import Extension as old_Extension

cxx_ext_re: Incomplete
fortran_pyf_ext_re: Incomplete

class Extension(old_Extension):
    sources: Incomplete
    swig_opts: Incomplete
    depends: Incomplete
    language: Incomplete
    f2py_options: Incomplete
    module_dirs: Incomplete
    extra_c_compile_args: Incomplete
    extra_cxx_compile_args: Incomplete
    extra_f77_compile_args: Incomplete
    extra_f90_compile_args: Incomplete
    def __init__(self, name, sources, include_dirs: Incomplete | None = None, define_macros: Incomplete | None = None, undef_macros: Incomplete | None = None, library_dirs: Incomplete | None = None, libraries: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, extra_objects: Incomplete | None = None, extra_compile_args: Incomplete | None = None, extra_link_args: Incomplete | None = None, export_symbols: Incomplete | None = None, swig_opts: Incomplete | None = None, depends: Incomplete | None = None, language: Incomplete | None = None, f2py_options: Incomplete | None = None, module_dirs: Incomplete | None = None, extra_c_compile_args: Incomplete | None = None, extra_cxx_compile_args: Incomplete | None = None, extra_f77_compile_args: Incomplete | None = None, extra_f90_compile_args: Incomplete | None = None) -> None: ...
    def has_cxx_sources(self): ...
    def has_f2py_sources(self): ...
