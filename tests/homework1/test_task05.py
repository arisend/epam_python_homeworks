from homework_01.hw.task05 import find_maximal_subarray_sum


def test_positive_case():
    """Testing correct tuple"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=3) == 18


def test_negative_case():
    """Testing wrong tuple"""
    assert not find_maximal_subarray_sum([-3, 30, 20, 50, 7], k=3) != 100
