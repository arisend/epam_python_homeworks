"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import unicodedata
from typing import List


def read_file_generator(file_path: str, encoding='utf-8', errors="ignore"):
    for row in open(file_path, "r", encoding=encoding, errors=errors):
        yield row


class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def metric(self):
        return len(set(self.value)) + len(self.value)


def tokenize(open_file):
    buffer = ""
    ascii = ''.join(chr(i) for i in range(128))
    for row in open_file:
        for i, symbol in enumerate(row):
            if unicodedata.category(symbol).startswith('L'):
                buffer += symbol
            elif symbol == '-' or (symbol == '\n' and row[i - 1] == "-"):
                yield Token(kind='symbol', value=symbol)

            else:
                if buffer:
                    yield Token(kind='word', value=buffer)
                    buffer = ''
                yield Token(kind='symbol', value=symbol)
            if unicodedata.category(symbol).startswith('P'):
                yield Token(kind='punctuation', value=symbol)
            if symbol not in ascii:
                yield Token(kind='non_ascii_char', value=symbol)


def get_longest_diverse_words(file_path: str, encoding="utf8", errors="ignore") -> List[str]:
    """
        This function read file and iteraterate by rows and tokens. Then it calculates the metric of length plus qty of
         unique symbols for each of the founded words and finally returns 10 words with max metric.
    :param errors:
    :param file_path:  Path to file for analysis
    :param encoding:  Encoding of file
    :return: List of 10 longest words consisting from largest amount of unique symbols
    :rtype: list
    """
    lst = list()
    for word in tokenize(read_file_generator(file_path, encoding=encoding, errors=errors)):
        if word.kind != "word":
            continue
        if not lst or len(lst) < 10:
            lst.append(word)
            lst = sorted(lst, key=lambda x: x.metric(), reverse=True)
        elif word.metric() > lst[9].metric():
            lst.pop()
            lst.append(word)
            lst = sorted(lst, key=lambda x: x.metric(), reverse=True)
        else:
            continue
    lst2 = list()
    for item in lst:
        lst2.append(item.value)
    return lst2


def get_rarest_chars(file_path: str, encoding="utf8", errors="ignore") -> list:
    """
         This function read file and iteraterate by rows and tokens. Find rarest symbols for document.
     :param errors:
     :param file_path:  Path to file for analysis
     :param encoding:  Encoding of file
     :return: list of rarest symbols for document
     :rtype: list
     """
    dct = dict()
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding, errors=errors)):
        if symbol.kind != "symbol":
            continue
        if symbol.value not in dct.keys():
            dct[symbol.value] = 1
        else:
            dct[symbol.value] = dct[symbol.value] + 1

    rarestcount = dct[next(iter(dct))]
    for key, value in dct.items():
        if rarestcount > value:
            rarestcount = value
    rarestlist = []
    for key, value in dct.items():
        if rarestcount == value:
            rarestlist.append(key)
    return rarestlist


def count_punctuation_chars(file_path: str, encoding="utf8", errors="ignore") -> int:
    """
             Count every punctuation char.
         :param errors:
         :param file_path:  Path to file for analysis
         :param encoding:  Encoding of file
         :return: Qty of punctuation chars in document
         :rtype: int
         """
    sum_punctuation = 0
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding, errors=errors)):
        if symbol.kind != "punctuation":
            continue
        sum_punctuation += 1
    return sum_punctuation


def count_non_ascii_chars(file_path: str, encoding="utf8", errors="ignore") -> int:
    """
             Count every non ascii char.
         :param errors:
         :param file_path:  Path to file for analysis
         :param encoding:  Encoding of file
         :return: Qty of non ascii chars in document
         :rtype: int
         """
    sum_non_ascii = 0
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding, errors=errors)):
        if symbol.kind != "non_ascii_char":
            continue
        sum_non_ascii += 1
    return sum_non_ascii


def get_most_common_non_ascii_char(file_path: str, encoding="utf8", errors="ignore") -> str:
    """
             Return most common non ascii char.
         :param errors:
         :param file_path:  Path to file for analysis
         :param encoding:  Encoding of file
         :return: Most common non ascii char
         :rtype: str
         """
    dct = dict()
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding, errors=errors)):
        if symbol.kind != "non_ascii_char":
            continue
        if symbol.value not in dct.keys():
            dct[symbol.value] = 1
        else:
            dct[symbol.value] = dct[symbol.value] + 1
    mostcommon = ''
    commontcount = 0
    for key, value in dct.items():
        if commontcount < value:
            mostcommon = key
            commontcount = value
    return mostcommon
