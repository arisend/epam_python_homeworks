from homework_07.hw.hw2 import backspace_compare


def test_negative_case():
    """Testing wrong cases"""
    assert backspace_compare("ab#c", "ad#c") is not False


def test_positive_case():
    """Testing correct cases"""
    assert backspace_compare("a##c", "#a#c") is True
    assert backspace_compare("a#c", "b") is False
