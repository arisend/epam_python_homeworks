"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Function that merges integer from sorted files and returns an iterator
    :param file_list:
    :return: Iterator with sorted values
    """

    generators_list = []
    for file in file_list:
        file_open = open(file, 'r')
        generators_list.append(file_open)
    iterators = [iter(it) for it in generators_list]
    values_dict = {}
    for it in iterators:
        values_dict[it] = None
    while True:
        for i, it in enumerate(iterators):
            try:
                if values_dict[it] is None:
                    values_dict[it] = next(it)
            except StopIteration:
                values_dict[it] = "END"
        if all(value == "END" for value in values_dict.values()):
            break
        min_it = min(values_dict, key=values_dict.get)
        yield values_dict[min_it].rstrip('\n')
        if values_dict[min_it] != "END":
            values_dict[min_it] = None
