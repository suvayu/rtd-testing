"""I/O for Foo"""

from .foo import Foo


def write_foo(obj: Foo, path: str):
    """Write :class:``Foo`` instance to ``path``."""
    return


def read_foo(path: str) -> Foo:
    """Read :class:``Foo`` from ``path``."""
    return Foo()
