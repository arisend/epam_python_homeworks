"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
for i in range(0, 1):
    pass


def custom_range(data, start=None, stop=None, step=1):
    result = []
    # print(start,stop)
    if step != 1 and step < 0:
        data = data[::step]
        start, stop = stop, start,
        for item in data:
            # print(item)
            if (start is not None and item > start) and (stop is not None and item <= stop):
                result.append(item)
            elif start is not None and stop is None and item > start:
                result.append(item)
            elif stop is not None and start is None and item <= stop:
                result.append(item)
    else:
        data = data[::step]
        for item in data:
            # print(item)
            if (start is not None and item >= start) and (stop is not None and item < stop):
                result.append(item)
            elif start is not None and stop is None and item >= start:
                result.append(item)
            elif stop is not None and start is None and item < stop:
                result.append(item)
    return result
