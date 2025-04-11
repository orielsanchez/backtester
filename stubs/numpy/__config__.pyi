from enum import Enum

__all__ = ['show_config']

class DisplayModes(Enum):
    stdout = 'stdout'
    dicts = 'dicts'

def show_config(mode=...): ...
