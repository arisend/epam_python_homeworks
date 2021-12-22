from homework_09.hw.hw2 import context_manager_func, context_manager_class


def test_positive_case():
    """Testing correct cases"""
    with context_manager_class(IndexError):
        [][2]
    with context_manager_func(IndexError):
        [][2]


def test_negative_case():
    """Testing wrong cases"""
    pass
