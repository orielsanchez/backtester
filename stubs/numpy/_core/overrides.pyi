from .._utils import set_module as set_module
from .._utils._inspect import getargspec as getargspec
from _typeshed import Incomplete
from numpy._core._multiarray_umath import add_docstring as add_docstring
from typing import NamedTuple

ARRAY_FUNCTIONS: Incomplete
array_function_like_doc: str

def get_array_function_like_doc(public_api, docstring_template: str = ''): ...
def finalize_array_function_like(public_api): ...

class ArgSpec(NamedTuple):
    args: Incomplete
    varargs: Incomplete
    keywords: Incomplete
    defaults: Incomplete

def verify_matching_signatures(implementation, dispatcher) -> None: ...
def array_function_dispatch(dispatcher: Incomplete | None = None, module: Incomplete | None = None, verify: bool = True, docs_from_dispatcher: bool = False): ...
def array_function_from_dispatcher(implementation, module: Incomplete | None = None, verify: bool = True, docs_from_dispatcher: bool = True): ...
