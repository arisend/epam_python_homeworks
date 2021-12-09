import pytest

from homework_01.hw.task03 import find_maximum_and_minimum




def test_positive_case():
    """Testing correct tuple"""
    assert find_maximum_and_minimum('list.txt')==(1,8)


def test_negative_case():
    """Testing wrong tuple"""
    assert not find_maximum_and_minimum('list2.txt')==(1,8)
