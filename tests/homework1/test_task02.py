from homework_01.hw.task02 import check_fibonacci


def test_positive_case():
    """Testing correct seq"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8])


def test_negative_case():
    """Testing wrong seq"""
    assert not check_fibonacci([0, 1, 1, 2, 4, 5, 8])
    assert not check_fibonacci([0, 0, 0, 0, 0, 0, 0])
    assert not check_fibonacci([-1, -1, -2, -3, -5])
    assert not check_fibonacci([2, 4, 6, 10])
