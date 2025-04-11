import abc
import enum
from abc import ABC, abstractmethod
from collections.abc import Iterable, Sequence
from typing import Any, TypedDict

class DlpackDeviceType(enum.IntEnum):
    CPU = 1
    CUDA = 2
    CPU_PINNED = 3
    OPENCL = 4
    VULKAN = 7
    METAL = 8
    VPI = 9
    ROCM = 10

class DtypeKind(enum.IntEnum):
    INT = 0
    UINT = 1
    FLOAT = 2
    BOOL = 20
    STRING = 21
    DATETIME = 22
    CATEGORICAL = 23

class ColumnNullType(enum.IntEnum):
    NON_NULLABLE = 0
    USE_NAN = 1
    USE_SENTINEL = 2
    USE_BITMASK = 3
    USE_BYTEMASK = 4

class ColumnBuffers(TypedDict):
    data: tuple[Buffer, Any]
    validity: tuple[Buffer, Any] | None
    offsets: tuple[Buffer, Any] | None

class CategoricalDescription(TypedDict):
    is_ordered: bool
    is_dictionary: bool
    categories: Column | None

class Buffer(ABC, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def bufsize(self) -> int: ...
    @property
    @abstractmethod
    def ptr(self) -> int: ...
    @abstractmethod
    def __dlpack__(self): ...
    @abstractmethod
    def __dlpack_device__(self) -> tuple[DlpackDeviceType, int | None]: ...

class Column(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def size(self) -> int: ...
    @property
    @abstractmethod
    def offset(self) -> int: ...
    @property
    @abstractmethod
    def dtype(self) -> tuple[DtypeKind, int, str, str]: ...
    @property
    @abstractmethod
    def describe_categorical(self) -> CategoricalDescription: ...
    @property
    @abstractmethod
    def describe_null(self) -> tuple[ColumnNullType, Any]: ...
    @property
    @abstractmethod
    def null_count(self) -> int | None: ...
    @property
    @abstractmethod
    def metadata(self) -> dict[str, Any]: ...
    @abstractmethod
    def num_chunks(self) -> int: ...
    @abstractmethod
    def get_chunks(self, n_chunks: int | None = None) -> Iterable[Column]: ...
    @abstractmethod
    def get_buffers(self) -> ColumnBuffers: ...

class DataFrame(ABC, metaclass=abc.ABCMeta):
    version: int
    @abstractmethod
    def __dataframe__(self, nan_as_null: bool = False, allow_copy: bool = True): ...
    @property
    @abstractmethod
    def metadata(self) -> dict[str, Any]: ...
    @abstractmethod
    def num_columns(self) -> int: ...
    @abstractmethod
    def num_rows(self) -> int | None: ...
    @abstractmethod
    def num_chunks(self) -> int: ...
    @abstractmethod
    def column_names(self) -> Iterable[str]: ...
    @abstractmethod
    def get_column(self, i: int) -> Column: ...
    @abstractmethod
    def get_column_by_name(self, name: str) -> Column: ...
    @abstractmethod
    def get_columns(self) -> Iterable[Column]: ...
    @abstractmethod
    def select_columns(self, indices: Sequence[int]) -> DataFrame: ...
    @abstractmethod
    def select_columns_by_name(self, names: Sequence[str]) -> DataFrame: ...
    @abstractmethod
    def get_chunks(self, n_chunks: int | None = None) -> Iterable[DataFrame]: ...
