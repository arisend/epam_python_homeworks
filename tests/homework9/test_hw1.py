import os.path
from homework_09.hw.hw1 import merge_sorted_files

path_to_file1 = os.path.join(os.path.dirname(__file__), 'file1.txt')
path_to_file2 = os.path.join(os.path.dirname(__file__), 'file2.txt')
path_to_file3 = os.path.join(os.path.dirname(__file__), 'file3.txt')


def test_positive_case():
    """Testing correct cases"""
    assert list(merge_sorted_files([path_to_file1, path_to_file2])) == ['1', '2', '3', '4', '5', '6']
    assert list(merge_sorted_files([path_to_file1, path_to_file3])) == ['1', '2', '3', '5', '8', '10', '12']


def test_negative_case():
    """Testing wrong cases"""
    assert list(merge_sorted_files([path_to_file1, path_to_file2])) != ['1', '2', '3', '8', '5', '10', '12']
