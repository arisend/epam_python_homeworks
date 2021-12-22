import os.path
from homework_08.hw.task1 import KeyValueStorage

path_to_file = os.path.join(os.path.dirname(__file__), 'task1.txt')


def test_positive_case():
    """Testing correct cases"""
    storage = KeyValueStorage(path_to_file)

    assert storage['name'] == 'kek'
    assert storage.song == 'shadilay'
    assert storage.power == 9001


def test_negative_case():
    """Testing wrong cases"""
    storage = KeyValueStorage(path_to_file)
    assert storage.last_name != ""
