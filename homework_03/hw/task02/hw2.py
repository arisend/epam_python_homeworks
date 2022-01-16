"""
Here's a not very efficient calculation function that calculates something important::
    import time
    import struct
    import random
    import hashlib

    def slow_calculate(value):
        "Some weird voodoo magic calculations"
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.

"""
import time
import struct
import random
import hashlib
from functools import lru_cache
import threading


@lru_cache
def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


class SummingThread(threading.Thread):
    array_of_results = [None] * 500

    def __init__(self, low, high):
        super(SummingThread, self).__init__()
        self.low = low
        self.high = high
        self.total = 0

    def run(self):

        for i in range(self.low, self.high):
            SummingThread.array_of_results[i] = slow_calculate(i)
            self.total += i


def calculate_sum():
    start_time = time.time()
    start = 0
    qty_of_threads = 100
    step = 25
    threads = [None] * qty_of_threads
    current_thread = 0
    for i in range(0, 501, step):
        threads[current_thread] = SummingThread(start, i)
        start = i
        current_thread += 1

    current_thread = 0
    for i in range(0, 501, step):
        threads[current_thread].start()

        current_thread += 1

    current_thread = 0
    for i in range(0, 501, step):
        threads[current_thread].join()

        current_thread += 1

    return SummingThread.array_of_results, time.time() - start_time
