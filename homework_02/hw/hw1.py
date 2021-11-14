"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
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