"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence, Generator


def fib_generator():
    """
    :return: Return infinitive fib generator
    :rtype: Generator
    """
    number = 0

    def fibonacci_of_pos(n):
        if n in {0, 1}:  # Base case
            return n
        return fibonacci_of_pos(n - 1) + fibonacci_of_pos(n - 2)  # recursive case

    while True:
        yield fibonacci_of_pos(number)
        number += 1


def _check_if_match_to_generator(lst: Sequence[int], gen: Generator):
    """
    Auxiliary function that checks if given list match to given fib generator
    :return: Return result of check
    :rtype: Bool
    """
    val = next(gen)
    while val < lst[0]:
        val = next(gen)
    if val == lst[0]:
        for item in lst[1:]:
            val = next(gen)
            if not item == val:
                return False
        return True
    else:
        return False


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Function that checks if given list consist of fib sequence
    :return: Return result of check
    :rtype: Bool
    """
    gen = fib_generator()
    return _check_if_match_to_generator(data, gen)
