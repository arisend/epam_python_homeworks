from homework_02.hw.hw1 import get_longest_diverse_words, get_rarest_chars, count_punctuation_chars, \
    count_non_ascii_chars, get_most_common_non_ascii_char


def test_positive_case():
    """Testing correct seq"""
    assert get_longest_diverse_words('data.txt', encoding='unicode-escape') == ['Souveränitätsansprüche',
                                                                                'symbolischsakramentale',
                                                                                'Verfassungsverletzungen',
                                                                                'Mehrheitsvorstellungen',
                                                                                'Werkstättenlandschaft',
                                                                                'politischstrategischen',
                                                                                'Werkstättenlandschaft',
                                                                                'Bevölkerungsabschub',
                                                                                'Wiederbelebungsübungen',
                                                                                'Kollektivschuldiger']
    assert get_rarest_chars('data.txt', encoding='unicode-escape') == ['›', '‹', '’', '(', ')']
    assert count_punctuation_chars('data.txt', encoding='unicode-escape') == 5475
    assert count_non_ascii_chars('data.txt', encoding='unicode-escape') == 2972
    assert get_most_common_non_ascii_char('data.txt', encoding='unicode-escape') == "ä"


def test_negative_case():
    """Testing wrong seq"""
    assert get_longest_diverse_words('data.txt', encoding='unicode-escape') != []
    assert get_rarest_chars('data.txt', encoding='unicode-escape') != []
    assert count_punctuation_chars('data.txt', encoding='unicode-escape') != 0
    assert count_non_ascii_chars('data.txt', encoding='unicode-escape') != 0
    assert get_most_common_non_ascii_char('data.txt', encoding='unicode-escape') != ""
