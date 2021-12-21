"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
with supressor(IndexError):
      [][2]
"""
from contextlib import contextmanager

@contextmanager
def context_manager_func(exception):
    try:
        yield
    except exception:
        pass
class context_manager_class:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        print("Entering Context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")
        return self.exception

with context_manager_class(IndexError):
    [][2]

with context_manager_func(IndexError):
    [][2]