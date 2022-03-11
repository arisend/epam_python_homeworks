import os

from homework_04.hw.task_1_read_file import read_magic_number

path_to_file_test1 = os.path.join(os.path.dirname(__file__), 'test1.txt')
path_to_file_test2 = os.path.join(os.path.dirname(__file__), 'test2.txt')


def test_negative_case():
    """Testing wrong case"""
    with open(path_to_file_test1, 'w') as outfile:
        outfile.write("Hey Mary.\n"
                      "1123")
    try:
        assert not read_magic_number(path_to_file_test1)
    except AssertionError:
        raise AssertionError
    finally:
        if os.path.lexists(path_to_file_test1):
            os.remove(path_to_file_test1)


def test_positive_case():
    """Testing correct case"""
    with open(path_to_file_test2, 'w') as outfile:
        outfile.write("2\n"
                      "1123")
    try:
        assert read_magic_number(path_to_file_test2)
    except AssertionError:
        raise AssertionError
    finally:
        if os.path.lexists(path_to_file_test2):
            os.remove(path_to_file_test2)
