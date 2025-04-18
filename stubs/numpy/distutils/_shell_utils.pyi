__all__ = ['WindowsParser', 'PosixParser', 'NativeParser']

class CommandLineParser:
    @staticmethod
    def join(argv) -> None: ...
    @staticmethod
    def split(cmd) -> None: ...

class WindowsParser:
    @staticmethod
    def join(argv): ...
    @staticmethod
    def split(cmd): ...

class PosixParser:
    @staticmethod
    def join(argv): ...
    @staticmethod
    def split(cmd): ...
NativeParser = WindowsParser
NativeParser = PosixParser
