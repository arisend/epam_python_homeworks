import os
import sys
import io
import functools
import pytest
import datetime

from homework_05.hw.save_original_info import save_function_decorator, print_result, custom_sum

custom_sum([1, 2, 3], [4, 5])
custom_sum(1, 2, 3, 4)

print(custom_sum.__doc__)
print(custom_sum.__name__)
without_print = custom_sum.__original_func
print(custom_sum.__original_func)
# the result returns without printing
without_print(1, 2, 3, 4)


def test_positive_case():
    """Testing correct case"""
    old_stdout = sys.stdout  # Memorize the default stdout stream
    sys.stdout = buffer = io.StringIO()
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)
    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    what_was_printed = buffer.getvalue()
    assert what_was_printed == """[1, 2, 3, 4, 5]
10
This function can sum any objects which have __add___
custom_sum
"""
    sys.stdout = old_stdout  # Put the old stream back in place
    buffer.close()


def test_negative_case():
    old_stdout = sys.stdout  # Memorize the default stdout stream
    sys.stdout = buffer = io.StringIO()
    print(custom_sum.__original_func)
    without_print(1, 2, 3, 4)
    what_was_printed = buffer.getvalue()
    assert """<function custom_sum at""" in what_was_printed and '10\n' not in what_was_printed
    sys.stdout = old_stdout  # Put the old stream back in place
    buffer.close()
