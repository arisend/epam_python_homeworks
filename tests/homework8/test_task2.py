import os.path
from homework_08.hw.task2 import TableData

path_to_file = os.path.join(os.path.dirname(__file__), 'example.sqlite')


def test_positive_case():
    """Testing correct cases"""
    presidents = TableData(database_name=path_to_file, table_name="presidents")
    assert len(presidents) == 3
    assert presidents['Yeltsin'] == ('Yeltsin', 999, 'Russia')
    assert ('Yeltsin' in presidents) is True
    lst = []
    for president in presidents:
        lst.append(president['name'])
    assert lst == ['Yeltsin', 'Trump', 'Big Man Tyrone']


def test_negative_case():
    """Testing wrong cases"""
    presidents = TableData(database_name=path_to_file, table_name="presidents")
    assert ('Putin' in presidents) is not True
