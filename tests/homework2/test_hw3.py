from homework_02.hw.hw3 import combinations, combinations2, combinations3


def test_positive_case():
    """Testing correct seq"""
    assert combinations([1, 2], [3, 4], [5, 6]) == [(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6),
                                                    (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6)]
    assert combinations2([1, 2], [3, 4], [5, 6]) == [[1, 3, 5],
                                                     [2, 3, 5],
                                                     [1, 4, 5],
                                                     [2, 4, 5],
                                                     [1, 3, 6],
                                                     [2, 3, 6],
                                                     [1, 4, 6],
                                                     [2, 4, 6]]
    assert combinations3([1, 2], [3, 4], [5, 6]) == [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6],
                                                     [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]


def test_negative_case():
    """Testing wrong seq"""
    pass
