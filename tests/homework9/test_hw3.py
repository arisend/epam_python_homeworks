import os.path
from homework_09.hw.hw3 import universal_file_counter

test_dir = os.path.dirname(__file__)


def test_positive_case():
    """Testing correct cases"""
    assert universal_file_counter(test_dir, 'txt') == 10
    assert universal_file_counter(test_dir, "txt", str.split) == 10


def test_negative_case():
    """Testing wrong cases"""
    assert universal_file_counter(test_dir, "csv", str.split) != 10
