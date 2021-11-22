"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List

def fizzbuzz_gen():
    current=1
    while True:
        if current  % 3==0 and current % 5==0:
            current+=1
            yield 'fizz buzz'
        elif current % 3==0:
            current += 1
            yield 'fizz'
        elif current % 5==0:
            current += 1
            yield 'buzz'
        else:
            currentr = current
            current += 1
            yield str(currentr)
def fizzbuzz(n: int) -> List[str]:
    """
    This function return list with length n with according to fizzbuzz game terms.
    It's uses infinite fizzbuzz_gen in order to generate limited sequence.
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(6.0)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz']
    >>> fizzbuzz(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """
    result=[]
    count=0
    gen = fizzbuzz_gen()
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    while count < n:
        result.append(next(gen))
        count+=1
    return result
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]


if __name__ == "__main__":
    import doctest
    doctest.testmod()