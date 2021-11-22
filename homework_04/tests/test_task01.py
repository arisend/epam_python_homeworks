import os
import sys
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent+'/hw')

from task_1_read_file import read_magic_number




def test_negative_case():
    """Testing wrong case"""
    with open(parent+'/hw/test1.txt', 'w') as outfile:
        outfile.write("Hey Mary.\n"
                      "1123")
    try:
        assert not read_magic_number(parent+'/hw/test1.txt')
    except AssertionError:
         raise AssertionError
    finally:
        if os.path.lexists(parent+'/hw/test1.txt'):
            os.remove(parent+'/hw/test1.txt')

def test_positive_case():
    """Testing correct case"""
    with open(parent+'/hw/test2.txt', 'w') as outfile:
        outfile.write("2\n"
                      "1123")
    try:
        assert read_magic_number(parent+'/hw/test2.txt')
    except AssertionError:
         raise AssertionError
    finally:
        if os.path.lexists(parent+'/hw/test2.txt'):
            os.remove(parent+'/hw/test2.txt')

