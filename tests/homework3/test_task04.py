from homework_03.hw.task04.task04 import is_armstrong


def test_positive_case():
    assert is_armstrong(153) is True, 'Is Armstrong number'


def test_negative_case():
    assert is_armstrong(10) is False, 'Is not Armstrong number'
