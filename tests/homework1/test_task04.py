from homework_01.hw.task04 import check_sum_of_four, check_sum_of_four2


def test_positive_case():
    """Testing correct tuple"""
    assert check_sum_of_four([], [], [], []) == 0
    assert check_sum_of_four2([], [], [], []) == 0


def test_negative_case():
    """Testing wrong tuple"""
    assert not check_sum_of_four([3], [-3], [10], [-10]) == 0
    assert not check_sum_of_four2([3], [-3], [10], [-10]) == 0
