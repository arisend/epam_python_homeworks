from homework_02.hw.hw2 import major_and_minor_elem


def test_positive_case():
    """Testing correct seq"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_negative_case():
    """Testing wrong seq"""
    assert major_and_minor_elem([3, 2, 3, 5, 5, 5]) != (3, 2)
