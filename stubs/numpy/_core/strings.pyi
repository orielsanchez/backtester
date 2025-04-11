from _typeshed import Incomplete
from numpy import add as add, equal as equal, greater as greater, greater_equal as greater_equal, less as less, less_equal as less_equal, not_equal as not_equal
from numpy._core.umath import isalnum as isalnum, isalpha as isalpha, isdecimal as isdecimal, isdigit as isdigit, islower as islower, isnumeric as isnumeric, isspace as isspace, istitle as istitle, isupper as isupper, str_len as str_len

__all__ = ['equal', 'not_equal', 'less', 'less_equal', 'greater', 'greater_equal', 'add', 'multiply', 'isalpha', 'isdigit', 'isspace', 'isalnum', 'islower', 'isupper', 'istitle', 'isdecimal', 'isnumeric', 'str_len', 'find', 'rfind', 'index', 'rindex', 'count', 'startswith', 'endswith', 'lstrip', 'rstrip', 'strip', 'replace', 'expandtabs', 'center', 'ljust', 'rjust', 'zfill', 'partition', 'rpartition', 'upper', 'lower', 'swapcase', 'capitalize', 'title', 'mod', 'decode', 'encode', 'translate']

def multiply(a, i): ...
def mod(a, values): ...
def find(a, sub, start: int = 0, end: Incomplete | None = None): ...
def rfind(a, sub, start: int = 0, end: Incomplete | None = None): ...
def index(a, sub, start: int = 0, end: Incomplete | None = None): ...
def rindex(a, sub, start: int = 0, end: Incomplete | None = None): ...
def count(a, sub, start: int = 0, end: Incomplete | None = None): ...
def startswith(a, prefix, start: int = 0, end: Incomplete | None = None): ...
def endswith(a, suffix, start: int = 0, end: Incomplete | None = None): ...
def decode(a, encoding: Incomplete | None = None, errors: Incomplete | None = None): ...
def encode(a, encoding: Incomplete | None = None, errors: Incomplete | None = None): ...
def expandtabs(a, tabsize: int = 8): ...
def center(a, width, fillchar: str = ' '): ...
def ljust(a, width, fillchar: str = ' '): ...
def rjust(a, width, fillchar: str = ' '): ...
def zfill(a, width): ...
def lstrip(a, chars: Incomplete | None = None): ...
def rstrip(a, chars: Incomplete | None = None): ...
def strip(a, chars: Incomplete | None = None): ...
def upper(a): ...
def lower(a): ...
def swapcase(a): ...
def capitalize(a): ...
def title(a): ...
def replace(a, old, new, count: int = -1): ...
def partition(a, sep): ...
def rpartition(a, sep): ...
def translate(a, table, deletechars: Incomplete | None = None): ...
