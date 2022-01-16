import os
from homework_01.hw.task03 import find_maximum_and_minimum


def test_positive_case():
    """Testing correct tuple"""
    path = os.path.join(os.path.dirname(__file__), 'list.txt')
    assert find_maximum_and_minimum(path) == (1, 8)


def test_negative_case():
    """Testing wrong tuple"""
    path = os.path.join(os.path.dirname(__file__), 'list2.txt')
    assert not find_maximum_and_minimum(path) == (1, 8)
