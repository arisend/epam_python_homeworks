from homework_03.hw.task03.hw3 import Filter, make_filter


def test_positive_even():
    """Testing positive_even"""
    # example of usage:
    rang = range(100)

    positive_even = Filter(lambda a: isinstance(a, int), lambda a: a > 0, lambda a: a % 2 == 0)
    positive_even.apply(rang)  # should return only even numbers from 0 to 99

    assert positive_even.apply(['s', 'f', 'g', '1', '2', 2, 4, 5]) == [2, 4]
    assert positive_even.apply(rang) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
                                         44,
                                         46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84,
                                         86,
                                         88, 90, 92, 94, 96, 98]


def test_make_filter():
    """Testing make_filter"""

    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly"
        }
    ]

    assert make_filter(name='polly', type='bird').apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird",
         "name": "polly"}]  # should return only second entry from the list
    assert make_filter(name='Bill', occupation='was here').apply(sample_data) == [
        {"name": "Bill", "last_name": "Gilbert", "occupation": "was here",
         "type": "person"}]  # should return only first entry from the list
