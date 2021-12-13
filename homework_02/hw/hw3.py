"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import product
from typing import List, Any
import logging


# root = logging.getLogger()
# root.setLevel(logging.DEBUG)
# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(message)s')
# handler.setFormatter(formatter)
# root.addHandler(handler)

def combinations(*args: List[Any]) -> List[List]:
    return list(product(*args))


def prod(lst, callcount):
    callcount += 1
    logging.debug("Entering function prod()")
    logging.debug("Parameters:\nl: {}".format(lst))
    if len(lst) == 1:
        logging.debug("End of recursion reached, returning {}".format(lst[0]))
        return lst[0]
    result = []
    if callcount == 1:
        for e in prod(lst[1:], callcount):
            for i in lst[0]:
                result.append([i, *e])
    else:
        for e in prod(lst[1:], callcount):
            for i in lst[0]:
                result.append([i, e])
    logging.debug("Returning {} , {}".format(result, callcount))
    return result


def combinations2(*args: List[Any]) -> List[List]:
    result = prod(args, 0)
    return result


def combinations3(*args: List[Any]) -> List[List]:
    pools = [tuple(pool) for pool in args]
    logging.debug(pools)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result
