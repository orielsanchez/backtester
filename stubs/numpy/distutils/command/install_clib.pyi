from _typeshed import Incomplete
from distutils.core import Command
from numpy.distutils.misc_util import get_cmd as get_cmd

class install_clib(Command):
    description: str
    user_options: Incomplete
    install_dir: Incomplete
    outfiles: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_outputs(self): ...
