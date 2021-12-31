from homework_11.hw.hw1 import ColorsEnum, SizesEnum


def test_colors_case():
    """Testing Colors class """
    assert ColorsEnum.RED == "RED"


def test_sizes_case():
    """Testing Sizes class """
    assert SizesEnum.XL == "XL"
