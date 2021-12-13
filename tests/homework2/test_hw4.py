from homework_02.hw.hw4 import cache


def test_positive_case():
    """Testing correct seq"""

    @cache
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2


def test_negative_case():
    """Testing wrong seq"""
    pass
