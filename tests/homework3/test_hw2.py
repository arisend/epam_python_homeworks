import os
import pytest
from homework_03.hw.task02.hw2 import calculate_sum

path_to_file_with_output = os.path.join(os.path.dirname(__file__), 'hw2_output.txt')


@pytest.fixture
def calculate_sum_fixture():
    return calculate_sum()


def test_result(calculate_sum_fixture):
    """Testing correct case"""
    with open(path_to_file_with_output, 'r') as file:
        assert str(calculate_sum_fixture[0]) == file.read()


def test_speed(calculate_sum_fixture):
    """Testing correct case"""
    assert calculate_sum_fixture[1] < 60
