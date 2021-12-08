"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0

    def get_root_or_leave(tree):
        if "__iter__" in tree.__dir__() and not isinstance(tree, str):
            if "items" in tree.__dir__():
                for leave in tree.items():
                    get_root_or_leave(leave)
            else:
                for leave in tree:
                    get_root_or_leave(leave)
        elif tree == element:
            nonlocal count
            count += 1

    get_root_or_leave(tree)
    return count


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
