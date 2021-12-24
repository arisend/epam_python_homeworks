import os
import sys
import io

from homework_05.hw.save_original_info import save_function_decorator, print_result, custom_sum

def test_positive_case():
    """Testing correct case"""
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    with open(path_to_file_with_output, 'r') as f:
        assert custom_sum.__doc__+ "\n" + custom_sum.__name__ == f.read()


def test_negative_case():
    old_stdout = sys.stdout  # Memorize the default stdout stream
    sys.stdout = buffer = io.StringIO()
    print(custom_sum.__original_func)
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    what_was_printed = buffer.getvalue()
    assert """<function custom_sum at""" in what_was_printed and '10\n' not in what_was_printed
    sys.stdout = old_stdout  # Put the old stream back in place
    buffer.close()
