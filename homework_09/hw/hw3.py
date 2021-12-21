"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import logging
from pathlib import Path
from typing import Optional, Callable
import os


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    count = 0
    for file in os.listdir(path=dir_path):
        if file.endswith(file_extension):
            logging.debug(file)
            with open(os.path.join(dir_path, file), '+r') as f_open:
                if not tokenizer:
                    count += len(f_open.readlines())
                else:
                    for line in f_open.readlines():
                        count += len(tokenizer(line))

    return count
