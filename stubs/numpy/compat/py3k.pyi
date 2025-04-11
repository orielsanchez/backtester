import os
import pickle as pickle
from _typeshed import Incomplete
from pathlib import Path as Path

__all__ = ['bytes', 'asbytes', 'isfileobj', 'getexception', 'strchar', 'unicode', 'asunicode', 'asbytes_nested', 'asunicode_nested', 'asstr', 'open_latin1', 'long', 'basestring', 'sixu', 'integer_types', 'is_pathlib_path', 'npy_load_module', 'Path', 'pickle', 'contextlib_nullcontext', 'os_fspath', 'os_PathLike']

long = int
integer_types: Incomplete
basestring = str
unicode = str
bytes = bytes

def asunicode(s): ...
def asbytes(s): ...
def asstr(s): ...
def isfileobj(f): ...
def open_latin1(filename, mode: str = 'r'): ...
def sixu(s): ...

strchar: str

def getexception(): ...
def asbytes_nested(x): ...
def asunicode_nested(x): ...
def is_pathlib_path(obj): ...

class contextlib_nullcontext:
    enter_result: Incomplete
    def __init__(self, enter_result: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *excinfo) -> None: ...

def npy_load_module(name, fn, info: Incomplete | None = None): ...

os_fspath: Incomplete
os_PathLike = os.PathLike
