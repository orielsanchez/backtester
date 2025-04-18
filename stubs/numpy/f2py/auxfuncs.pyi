import pprint
from .cfuncs import errmess as errmess
from _typeshed import Incomplete

__all__ = ['applyrules', 'debugcapi', 'dictappend', 'errmess', 'gentitle', 'getargs2', 'getcallprotoargument', 'getcallstatement', 'getfortranname', 'getpymethoddef', 'getrestdoc', 'getusercode', 'getusercode1', 'getdimension', 'hasbody', 'hascallstatement', 'hascommon', 'hasexternals', 'hasinitvalue', 'hasnote', 'hasresultnote', 'isallocatable', 'isarray', 'isarrayofstrings', 'ischaracter', 'ischaracterarray', 'ischaracter_or_characterarray', 'iscomplex', 'iscstyledirective', 'iscomplexarray', 'iscomplexfunction', 'iscomplexfunction_warn', 'isdouble', 'isdummyroutine', 'isexternal', 'isfunction', 'isfunction_wrap', 'isint1', 'isint1array', 'isinteger', 'isintent_aux', 'isintent_c', 'isintent_callback', 'isintent_copy', 'isintent_dict', 'isintent_hide', 'isintent_in', 'isintent_inout', 'isintent_inplace', 'isintent_nothide', 'isintent_out', 'isintent_overwrite', 'islogical', 'islogicalfunction', 'islong_complex', 'islong_double', 'islong_doublefunction', 'islong_long', 'islong_longfunction', 'ismodule', 'ismoduleroutine', 'isoptional', 'isprivate', 'isvariable', 'isrequired', 'isroutine', 'isscalar', 'issigned_long_longarray', 'isstring', 'isstringarray', 'isstring_or_stringarray', 'isstringfunction', 'issubroutine', 'get_f2py_modulename', 'issubroutine_wrap', 'isthreadsafe', 'isunsigned', 'isunsigned_char', 'isunsigned_chararray', 'isunsigned_long_long', 'isunsigned_long_longarray', 'isunsigned_short', 'isunsigned_shortarray', 'l_and', 'l_not', 'l_or', 'outmess', 'replace', 'show', 'stripcomma', 'throw_error', 'isattr_value', 'getuseblocks', 'process_f2cmap_dict', 'containscommon']

show = pprint.pprint

def outmess(t) -> None: ...
def debugcapi(var): ...
def ischaracter_or_characterarray(var): ...
def ischaracter(var): ...
def ischaracterarray(var): ...
def isstring_or_stringarray(var): ...
def isstring(var): ...
def isstringarray(var): ...
def isarrayofstrings(var): ...
def isarray(var): ...
def isscalar(var): ...
def iscomplex(var): ...
def islogical(var): ...
def isinteger(var): ...
def isint1(var): ...
def islong_long(var): ...
def isunsigned_char(var): ...
def isunsigned_short(var): ...
def isunsigned(var): ...
def isunsigned_long_long(var): ...
def isdouble(var): ...
def islong_double(var): ...
def islong_complex(var): ...
def iscomplexarray(var): ...
def isint1array(var): ...
def isunsigned_chararray(var): ...
def isunsigned_shortarray(var): ...
def isunsigned_long_longarray(var): ...
def issigned_long_longarray(var): ...
def isallocatable(var): ...
def ismoduleroutine(rout): ...
def ismodule(rout): ...
def isfunction(rout): ...
def isfunction_wrap(rout): ...
def issubroutine(rout): ...
def issubroutine_wrap(rout): ...
def isattr_value(var): ...
def isroutine(rout): ...
def islogicalfunction(rout): ...
def islong_longfunction(rout): ...
def islong_doublefunction(rout): ...
def iscomplexfunction(rout): ...
def iscomplexfunction_warn(rout): ...
def isstringfunction(rout): ...
def hasexternals(rout): ...
def isthreadsafe(rout): ...
def isoptional(var): ...
def isexternal(var): ...
def getdimension(var): ...
def isrequired(var): ...
def iscstyledirective(f2py_line): ...
def isintent_in(var): ...
def isintent_inout(var): ...
def isintent_out(var): ...
def isintent_hide(var): ...
def isintent_nothide(var): ...
def isintent_c(var): ...
def isintent_copy(var): ...
def isintent_overwrite(var): ...
def isintent_callback(var): ...
def isintent_inplace(var): ...
def isintent_aux(var): ...

isintent_dict: Incomplete

def isprivate(var): ...
def isvariable(var): ...
def hasinitvalue(var): ...
def hasnote(var): ...
def hasresultnote(rout): ...
def hascommon(rout): ...
def containscommon(rout): ...
def hasbody(rout): ...
def hascallstatement(rout): ...

class F2PYError(Exception): ...

class throw_error:
    mess: Incomplete
    def __init__(self, mess) -> None: ...
    def __call__(self, var) -> None: ...

def l_and(*f): ...
def l_or(*f): ...
def l_not(f): ...
def isdummyroutine(rout): ...
def getfortranname(rout): ...
def getcallstatement(rout): ...
def getcallprotoargument(rout, cb_map={}): ...
def getusercode(rout): ...
def getusercode1(rout): ...
def getpymethoddef(rout): ...
def getargs2(rout): ...
def getrestdoc(rout): ...
def gentitle(name): ...
def stripcomma(s): ...
def replace(str, d, defaultsep: str = ''): ...
def dictappend(rd, ar): ...
def applyrules(rules, d, var={}): ...
def get_f2py_modulename(source): ...
def getuseblocks(pymod): ...
def process_f2cmap_dict(f2cmap_all, new_map, c2py_map, verbose: bool = False): ...
