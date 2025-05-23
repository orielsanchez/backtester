from _typeshed import Incomplete
from typing import Callable

def get_keywords(): ...

class VersioneerConfig: ...

def get_config(): ...

class NotThisMethod(Exception): ...

LONG_VERSION_PY: dict[str, str]
HANDLERS: dict[str, dict[str, Callable]]

def register_vcs_handler(vcs, method): ...
def run_command(commands, args, cwd: Incomplete | None = None, verbose: bool = False, hide_stderr: bool = False, env: Incomplete | None = None): ...
def versions_from_parentdir(parentdir_prefix, root, verbose): ...
def git_get_keywords(versionfile_abs): ...
def git_versions_from_keywords(keywords, tag_prefix, verbose): ...
def git_pieces_from_vcs(tag_prefix, root, verbose, runner=...): ...
def plus_or_dot(pieces) -> str: ...
def render_pep440(pieces): ...
def render_pep440_branch(pieces): ...
def pep440_split_post(ver): ...
def render_pep440_pre(pieces): ...
def render_pep440_post(pieces): ...
def render_pep440_post_branch(pieces): ...
def render_pep440_old(pieces): ...
def render_git_describe(pieces): ...
def render_git_describe_long(pieces): ...
def render(pieces, style): ...
def get_versions(): ...
