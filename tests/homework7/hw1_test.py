from homework_07.hw.hw1 import find_occurrences, example_tree


def test_negative_case():
    """Testing wrong cases"""
    assert find_occurrences(example_tree, "simple_key") != 0
    assert find_occurrences(example_tree, "abc") != 0


def test_positive_case():
    """Testing correct cases"""
    assert find_occurrences(example_tree, "RED") == 6  # 6
    assert find_occurrences(example_tree, "BLUE") == 2
