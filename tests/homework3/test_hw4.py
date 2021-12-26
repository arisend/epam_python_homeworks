import pytest
from functools import partial
from homework_03.hw.task01.hw4 import cache


@pytest.fixture
def prepare_func():
    cache3 = partial(cache, times=3)

    @cache3
    def func(a, b):
        return (a ** b) ** 2

    return func


def test_positive_case(prepare_func):
    """Testing correct case"""

    some = 100, 200

    val_1 = prepare_func(*some)
    val_2 = prepare_func(*some)
    val_3 = prepare_func(*some)

    assert val_1 is val_2
    assert val_1 is val_3


def test_negative_case(prepare_func):
    some = 100, 200

    val_1 = prepare_func(*some)
    prepare_func(*some)
    prepare_func(*some)
    val_4 = prepare_func(*some)

    assert val_1 is not val_4
