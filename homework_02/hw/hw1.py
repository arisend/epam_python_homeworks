"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
<<<<<<< Updated upstream
from typing import List
import re
import pandas as pd

def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r+") as ouf:
        file_data = ouf.read()
        file_data=file_data.encode().decode('unicode-escape')
        words = re.findall(r'\w+-\n{,1}\w{,20}', file_data)
        words2 = re.findall(r'\w+', file_data)
        words=words+words2
        words=set(words)
        listwords=[]
        listuniquiecount=[]
        listlencount=[]
        for word in words:
            wordre=word.replace('-\n','').replace('-','')
            if re.search('\d+', wordre) is None:
                pass
                listwords.append(wordre)
                listuniquiecount.append(len(set(wordre)))
                listlencount.append(len(wordre))
        df=pd.DataFrame({'words' : listwords, 'unique' : listuniquiecount , 'len':listlencount})
        top10=df.sort_values(by=['unique', 'len'], ascending=False).head(10)
        print(top10['words'].values)
        return top10['words'].values
#get_longest_diverse_words('data.txt')

def get_rarest_chars(file_path: str) -> str:
    with open(file_path, "r+") as ouf:
        file_data = ouf.read()
        file_data = file_data.encode().decode('unicode-escape')
        list_of_chars=list(set(file_data))
        count_of_chars=[]
        for item in list_of_chars:
            count=0
            for char in file_data:
                if char == item:
                    count = count + 1
            count_of_chars.append(count)
        df = pd.DataFrame({'chars': list_of_chars, 'counter': count_of_chars})
        #print(df.sort_values(by=['counter'], ascending=True))
        dffilteredlist=df[df['counter']==1]['chars'].to_list()
        str_to_return=""
        for char in dffilteredlist:
            str_to_return+=char
        print(str_to_return)
        return str_to_return
#get_rarest_chars('data.txt')

def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r+") as ouf:
        file_data = ouf.read()
        file_data = file_data.encode().decode('unicode-escape')
        list_punc_char=[ '\n', '›',  '—', ':', "'", ';', '?', '(', '‹', '«', ' ', ')', '»', '.', '-', ',', '’']
        count_of_chars = []
        for item in list_punc_char:
            count = 0
            for char in file_data:
                if char == item:
                    count = count + 1
            count_of_chars.append(count)
        df = pd.DataFrame({'chars': list_punc_char, 'counter': count_of_chars})
        dfsorted=df.sort_values(by=['counter'], ascending=True)
        sum=dfsorted['counter'].sum()
        print(sum)
        return sum
#count_punctuation_chars('data.txt')

def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r+") as ouf:
        file_data = ouf.read()
        file_data = file_data.encode().decode('unicode-escape')
        set_of_chars = set(file_data)
        #print(set_of_chars)
        new_set_of_chars=set_of_chars.copy()
        for char in set_of_chars:
            if char in ''.join(chr(i) for i in range(128)):
                new_set_of_chars.remove(char)

        #print(new_set_of_chars)
        list_of_chars=list(new_set_of_chars)
        count_of_chars = []
        for item in list_of_chars:
            count = 0
            for char in file_data:
                if char == item:
                    count = count + 1
            count_of_chars.append(count)
        df = pd.DataFrame({'chars': list_of_chars, 'counter': count_of_chars})
        dfsorted=df.sort_values(by=['counter'], ascending=True)
        sum=dfsorted['counter'].sum()
        print(sum)
        return sum
#count_non_ascii_chars('data.txt')

def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r+") as ouf:
        file_data = ouf.read()
        file_data = file_data.encode().decode('unicode-escape')
        set_of_chars = set(file_data)
        # print(set_of_chars)
        new_set_of_chars = set_of_chars.copy()
        for char in set_of_chars:
            if char in ''.join(chr(i) for i in range(128)):
                new_set_of_chars.remove(char)

        # print(new_set_of_chars)
        list_of_chars = list(new_set_of_chars)
        count_of_chars = []
        for item in list_of_chars:
            count = 0
            for char in file_data:
                if char == item:
                    count = count + 1
            count_of_chars.append(count)
        df = pd.DataFrame({'chars': list_of_chars, 'counter': count_of_chars})
        # print(df.sort_values(by=['counter'], ascending=True))
        top1 = df.sort_values(by=['counter'], ascending=False).head(1)['chars'].values[0]
        print(top1)
        return top1
#get_most_common_non_ascii_char('data.txt')
=======
import unicodedata
from typing import List


def read_file_generator(file_path: str, encoding='utf-8'):
    for row in open(file_path, "r", encoding=encoding):
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


def get_longest_diverse_words(file_path: str, encoding="utf8") -> List[str]:
    """
        This function read file and iteraterate by rows and tokens. Then it calculates the metric of length plus qty of
         unique symbols for each of the founded words and finally returns 10 words with max metric.
    :param file_path:  Path to file for analysis
    :param encoding:  Encoding of file
    :return: List of 10 longest words consisting from largest amount of unique symbols
    :rtype: list
    """
    lst = list()
    for word in tokenize(read_file_generator(file_path, encoding=encoding)):
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


def get_rarest_chars(file_path: str, encoding="utf8") -> list:
    """
         This function read file and iteraterate by rows and tokens. Find rarest symbols for document.
     :param file_path:  Path to file for analysis
     :param encoding:  Encoding of file
     :return: list of rarest symbols for document
     :rtype: list
     """
    dct = dict()
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding)):
        if symbol.kind != "symbol":
            continue
        if symbol.value not in dct.keys():
            dct[symbol.value] = 1
        else:
            dct[symbol.value] = dct[symbol.value] + 1
    rarest = ''
    rarestcount = dct[next(iter(dct))]
    for key, value in dct.items():
        if rarestcount > value:
            rarest = key
            rarestcount = value
    rarestlist = []
    for key, value in dct.items():
        if rarestcount == value:
            rarestlist.append(key)
    return rarestlist


def count_punctuation_chars(file_path: str, encoding="utf8") -> int:
    """
             Count every punctuation char.
         :param file_path:  Path to file for analysis
         :param encoding:  Encoding of file
         :return: Qty of punctuation chars in document
         :rtype: int
         """
    sum_punctuation = 0
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding)):
        if symbol.kind != "punctuation":
            continue
        sum_punctuation += 1
    return sum_punctuation


def count_non_ascii_chars(file_path: str, encoding="utf8") -> int:
    """
             Count every non ascii char.
         :param file_path:  Path to file for analysis
         :param encoding:  Encoding of file
         :return: Qty of non ascii chars in document
         :rtype: int
         """
    sum_non_ascii = 0
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding)):
        if symbol.kind != "non_ascii_char":
            continue
        sum_non_ascii += 1
    return sum_non_ascii


def get_most_common_non_ascii_char(file_path: str, encoding="utf8") -> str:
    """
             Return most common non ascii char.
         :param file_path:  Path to file for analysis
         :param encoding:  Encoding of file
         :return: Most common non ascii char
         :rtype: str
         """
    dct = dict()
    for symbol in tokenize(read_file_generator(file_path, encoding=encoding)):
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
>>>>>>> Stashed changes
