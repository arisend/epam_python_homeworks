"""
We have a file that works as key-value storage, each line is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name']  # will be string 'kek'
storage.song_name  # will be 'shadilay'
storage.power  # will be integer 9001

In case of attribute clash existing built-in attributes take precedence. In case when value cannot be assigned to an
attribute (for example when there's a line `1=something`) ValueError should be raised. File size is expected to be
small, you are permitted to read it entirely into memory.

"""
import unicodedata


def read_file_generator(file_path: str, encoding='utf-8', errors="ignore"):
    for row in open(file_path, "r", encoding=encoding, errors=errors):
        yield row


class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value


def tokenize(open_file):
    buffer = ""
    buffer2 = ""
    for row in open_file:
        for i, symbol in enumerate(row):
            if unicodedata.category(symbol).startswith('L') or symbol == "_":
                buffer += symbol
            elif buffer and unicodedata.category(symbol).startswith('N'):
                buffer += symbol
            elif not buffer and unicodedata.category(symbol).startswith('N'):
                buffer2 += symbol
            elif buffer2 and symbol == ".":
                buffer2 += symbol
            elif symbol == "=":
                if buffer:
                    yield Token(kind='word_key', value=buffer)
                    buffer = ''
                else:
                    yield Token(kind='unexpected_symbol', value=symbol)
            elif symbol == "\n":
                if buffer:
                    yield Token(kind='word_value', value=buffer)
                    buffer = ''
                if buffer2:
                    yield Token(kind='number_value', value=buffer2)
                    buffer2 = ''
            else:
                yield Token(kind='unexpected_symbol', value=symbol)


class KeyValueStorage:
    """
    wrapper class for  key value storage that works like this:
    storage = KeyValueStorage('path_to_file.txt')
    keys and values accessible as collection items and as attributes.
    Example:
    storage['name']  # will be string 'kek'
    storage.song_name  # will be 'shadilay'
    storage.power  # will be integer 9001
    """
    def __getitem__(self, key):
        return getattr(self, key)

    def __init__(self, path_to_file):
        __slots__ = []
        lastkey = None
        for item in tokenize(read_file_generator(path_to_file)):
            if item.kind == 'unexpected_symbol':
                raise ValueError("Got unexpected symbol from the file '{}'.".format(item.value))

            elif item.kind == 'word_key':
                if item.value not in self.__dict__:
                    __slots__.append(item.value)
                lastkey = item.value

            elif lastkey and (item.kind == 'word_value' or item.kind == 'number_value'):
                if item.kind == 'word_value':
                    setattr(self, lastkey, item.value)
                    lastkey = None
                else:
                    setattr(self, lastkey, float(item.value))
                    lastkey = None
            else:
                raise ValueError("Got wrong quantity of values.")
