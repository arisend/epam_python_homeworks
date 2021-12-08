from homework_07.hw.hw3 import tic_tac_toe_checker


def test_negative_case():
    """Testing wrong cases"""
    assert tic_tac_toe_checker([['-', '-', 'o'], ['-', 'o', 'o'], ['x', 'x', 'x']]) != "o wins!"


def test_positive_case():
    """Testing correct cases"""
    assert tic_tac_toe_checker([['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']]) == "unfinished"
