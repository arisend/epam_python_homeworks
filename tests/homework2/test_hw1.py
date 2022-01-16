import os.path

from homework_02.hw.hw1 import get_longest_diverse_words, get_rarest_chars, count_punctuation_chars, \
    count_non_ascii_chars, get_most_common_non_ascii_char

path_to_file = os.path.join(os.path.dirname(__file__), 'data.txt')


def test_positive_case():
    """Testing correct cases"""
    assert get_longest_diverse_words(path_to_file, encoding='unicode-escape') == ['Souveränitätsansprüche',
                                                                                  'symbolischsakramentale',
                                                                                  'Verfassungsverletzungen',
                                                                                  'Mehrheitsvorstellungen',
                                                                                  'Werkstättenlandschaft',
                                                                                  'politischstrategischen',
                                                                                  'Werkstättenlandschaft',
                                                                                  'Bevölkerungsabschub',
                                                                                  'Wiederbelebungsübungen',
                                                                                  'Kollektivschuldiger']
    assert get_rarest_chars(path_to_file, encoding='unicode-escape') == ['›', '‹', '’', '(', ')']
    assert count_punctuation_chars(path_to_file, encoding='unicode-escape') == 5475
    assert count_non_ascii_chars(path_to_file, encoding='unicode-escape') == 2972
    assert get_most_common_non_ascii_char(path_to_file, encoding='unicode-escape') == "ä"


def test_negative_case():
    """Testing wrong cases"""
    assert get_longest_diverse_words(path_to_file, encoding='unicode-escape') != []
    assert get_rarest_chars(path_to_file, encoding='unicode-escape') != []
    assert count_punctuation_chars(path_to_file, encoding='unicode-escape') != 0
    assert count_non_ascii_chars(path_to_file, encoding='unicode-escape') != 0
    assert get_most_common_non_ascii_char(path_to_file, encoding='unicode-escape') != ""
