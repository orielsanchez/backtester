def check_inline(cmd): ...
def check_restrict(cmd): ...
def check_compiler_gcc(cmd): ...
def check_gcc_version_at_least(cmd, major, minor: int = 0, patchlevel: int = 0): ...
def check_gcc_function_attribute(cmd, attribute, name): ...
def check_gcc_function_attribute_with_intrinsics(cmd, attribute, name, code, include): ...
def check_gcc_variable_attribute(cmd, attribute): ...
