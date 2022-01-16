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
from functools import wraps


def cache(function: Callable, times) -> Callable:
    """
    This function implement decorator which save result of called function first time in cache
    and then return saved value specified qty of times.
    :param function:
    :param times:
    :return: wrapper
    """
    cache_dict = {}

    @wraps(function)
    def wrapper(*args):
        if args in cache_dict and cache_dict[args][1] < times:
            cache_dict[args][1] += 1
            return cache_dict[args][0]
        else:
            val = function(*args)
            cache_dict[args] = [val, 1, function]

            return val

    return wrapper
