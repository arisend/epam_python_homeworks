import string
from homework_02.hw.hw5 import custom_range


def test_positive_case():
    """Testing correct seq"""
    assert custom_range(string.ascii_lowercase, stop='g') == ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']


def test_negative_case():
    """Testing wrong seq"""
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) != ['p', 'j', 'h']
