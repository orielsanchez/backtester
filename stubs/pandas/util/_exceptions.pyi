from collections.abc import Generator

def rewrite_exception(old_name: str, new_name: str) -> Generator[None, None, None]: ...
def find_stack_level() -> int: ...
def rewrite_warning(target_message: str, target_category: type[Warning], new_message: str, new_category: type[Warning] | None = None) -> Generator[None, None, None]: ...
