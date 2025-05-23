import numpy.ma as ma
from _typeshed import Incomplete

__all__ = ['MaskedRecords', 'mrecarray', 'fromarrays', 'fromrecords', 'fromtextfile', 'addfield']

class MaskedRecords(ma.MaskedArray):
    def __new__(cls, shape, dtype: Incomplete | None = None, buf: Incomplete | None = None, offset: int = 0, strides: Incomplete | None = None, formats: Incomplete | None = None, names: Incomplete | None = None, titles: Incomplete | None = None, byteorder: Incomplete | None = None, aligned: bool = False, mask=..., hard_mask: bool = False, fill_value: Incomplete | None = None, keep_mask: bool = True, copy: bool = False, **options): ...
    def __array_finalize__(self, obj) -> None: ...
    def __len__(self) -> int: ...
    def __getattribute__(self, attr): ...
    def __setattr__(self, attr, val): ...
    def __getitem__(self, indx): ...
    def __setitem__(self, indx, value) -> None: ...
    def view(self, dtype: Incomplete | None = None, type: Incomplete | None = None): ...
    def harden_mask(self) -> None: ...
    def soften_mask(self) -> None: ...
    def copy(self): ...
    def tolist(self, fill_value: Incomplete | None = None): ...
    def __reduce__(self): ...
mrecarray = MaskedRecords

def fromarrays(arraylist, dtype: Incomplete | None = None, shape: Incomplete | None = None, formats: Incomplete | None = None, names: Incomplete | None = None, titles: Incomplete | None = None, aligned: bool = False, byteorder: Incomplete | None = None, fill_value: Incomplete | None = None): ...
def fromrecords(reclist, dtype: Incomplete | None = None, shape: Incomplete | None = None, formats: Incomplete | None = None, names: Incomplete | None = None, titles: Incomplete | None = None, aligned: bool = False, byteorder: Incomplete | None = None, fill_value: Incomplete | None = None, mask=...): ...
def fromtextfile(fname, delimiter: Incomplete | None = None, commentchar: str = '#', missingchar: str = '', varnames: Incomplete | None = None, vartypes: Incomplete | None = None, *, delimitor=...): ...
def addfield(mrecord, newfield, newfieldname: Incomplete | None = None): ...
