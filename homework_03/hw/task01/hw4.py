"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'

"""
from typing import Callable
from functools import partial, wraps


def cache(func: Callable, times) -> Callable:
    cache = {}
    global attempnumber
    attempnumber = 1
    @wraps(func)
    def wrapper(*args):
        global attempnumber
        if args in cache and attempnumber < times:
            attempnumber += 1
            return cache[args]
        else:
            val = func(*args)
            cache[args] = val
            return val
    return wrapper


cache3 = partial(cache, times=3)


@cache3
def func(a, b):
    print(a, b)
    return (a ** b) ** 2


cache_func = cache3(func)
some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)
val_3 = cache_func(*some)
val_4 = cache_func(*some)

assert val_1 is val_2
assert val_1 is val_3
assert val_1 is not val_4
