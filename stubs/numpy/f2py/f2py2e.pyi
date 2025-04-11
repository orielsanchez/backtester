import argparse
import pprint
from . import __version__ as __version__, auxfuncs as auxfuncs, capi_maps as capi_maps, cb_rules as cb_rules, cfuncs as cfuncs, crackfortran as crackfortran, f90mod_rules as f90mod_rules, rules as rules
from .cfuncs import errmess as errmess
from _typeshed import Incomplete
from numpy.f2py._backends import f2py_build_generator as f2py_build_generator

f2py_version: Incomplete
numpy_version: Incomplete
show = pprint.pprint
outmess = auxfuncs.outmess
MESON_ONLY_VER: Incomplete
__usage__: Incomplete

def scaninputline(inputline): ...
def callcrackfortran(files, options): ...
def buildmodules(lst): ...
def dict_append(d_out, d_in) -> None: ...
def run_main(comline_list): ...
def filter_files(prefix, suffix, files, remove_prefix: Incomplete | None = None): ...
def get_prefix(module): ...

class CombineIncludePaths(argparse.Action):
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None: ...

def f2py_parser(): ...
def get_newer_options(iline): ...
def make_f2py_compile_parser(): ...
def preparse_sysargv(): ...
def run_compile() -> None: ...
def validate_modulename(pyf_files, modulename: str = 'untitled'): ...
def main() -> None: ...
