"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    inpset=set(inp)
    minor = {'elem': None, 'count': len(inp)+1}
    major = {'elem': None, 'count': 0}
    for elem in inpset:
        count=0
        for el in inp:
            if elem==el:
                count+=1
        if count>len(inp)//2 and count>major['count']:
            major={'elem':elem,'count':count}
        if count<minor['count']:
            minor={'elem':elem,'count':count}
    return (major['elem'],minor['elem'])
print(major_and_minor_elem([3,2,3]))
print(major_and_minor_elem([2,2,1,1,1,2,2]))