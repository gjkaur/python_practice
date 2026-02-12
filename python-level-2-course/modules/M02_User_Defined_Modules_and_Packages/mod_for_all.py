"""Module demonstrating __all__ for Practice 3."""

__all__ = ["public_func"]


def public_func():
    """Public function - exported by 'from mod_for_all import *'."""
    pass


def _private_helper():
    """Private helper - NOT exported by 'from mod_for_all import *'."""
    pass
