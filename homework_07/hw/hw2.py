"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str):
    first_res = ""
    for pos, item in enumerate(first):
        # print(pos)
        if item != "#" and (len(first) == int(pos) + 1 or first[int(pos) + 1] != "#"):
            first_res += item
    second_res = ""
    for pos, item in enumerate(second):
        if item != "#" and (len(second) == int(pos) + 1 or second[int(pos) + 1] != "#"):
            second_res += item

    return first_res == second_res
