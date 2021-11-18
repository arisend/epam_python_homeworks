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
start_time = time.time()

@lru_cache
def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


array_of_results=[None]* 500


class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0
     # def run(self):
     #     for i in range(self.low,self.high):
     #         self.total+=i
     #
     def run(self):
         global array_of_results
         for i in range(self.low, self.high):
             #print(i)
             array_of_results[i] = slow_calculate(i)
             self.total += i

start=0
qty_of_threads=21
step=25
threads=[None]*qty_of_threads
currthread=0
for i in range(0,501,step):
    threads[currthread]=SummingThread(start,i)
    start=i
    currthread+=1
start=0
currthread=0
for i in range(0,501,step):
    threads[currthread].start()
    start=i
    currthread+=1
start=0
currthread=0
for i in range(0,501,step):
    threads[currthread].join()
    start=i
    currthread+=1


print(array_of_results)

print("--- %s seconds ---" % (time.time() - start_time))

"""
[2785, 1996, 1647, 2698, 2135, 2028, 1827, 2070, 2441, 2219, 1989, 1880, 2282, 2033, 2123, 2358, 2160, 2242, 1690, 2282, 1721, 1756, 2097, 2404, 1879, 1874, 1919, 2438, 1882, 1707, 1985, 1946, 2174, 2094, 2468, 1776, 1605, 2750, 2589, 2181, 2281, 2286, 2089, 2125, 2342, 1980, 2709, 2766, 1717, 2332, 2174, 1801, 2225, 1934, 2339, 1538, 2225, 2153, 2089, 1779, 1630, 2327, 2191, 2151, 1439, 2202, 2483, 1948, 2303, 1870, 1889, 2223, 2349, 2580, 2022, 1936, 2287, 1632, 2504, 2200, 1560, 1965, 1768, 2623, 2008, 1716, 2574, 2400, 1722, 1946, 2184, 2012, 1993, 2063, 2517, 2368, 1945, 2528, 1828, 2070, 2219, 2239, 2466, 2327, 2214, 2247, 2310, 1890, 2108, 2154, 2164, 1778, 1748, 2140, 2619, 1729, 2008, 2204, 2541, 2092, 2211, 2439, 1939, 1238, 2441, 2247, 1979, 2545, 2329, 2131, 1767, 2501, 2138, 1951, 1556, 1568, 2055, 2429, 2325, 2166, 1868, 2083, 2313, 2147, 1892, 1828, 1816, 1959, 1748, 2475, 2165, 2184, 2019, 2810, 2093, 2274, 2497, 1748, 1635, 1719, 2217, 2223, 1681, 2091, 2529, 2176, 2192, 2010, 1863, 2046, 2022, 2322, 1951, 1962, 2163, 1806, 1813, 2016, 2160, 2152, 1684, 1997, 1641, 2448, 2133, 2081, 2508, 1562, 1932, 1630, 2047, 1905, 2420, 2110, 2064, 1836, 1943, 2166, 1887, 2349, 1915, 2114, 1917, 2611, 2191, 2019, 2450, 2659, 1780, 1423, 2380, 1764, 1382, 2100, 1936, 2202, 2457, 2171, 2543, 2028, 2207, 1428, 2009, 1448, 1755, 2082, 1841, 1957, 1655, 1616, 2053, 1898, 2215, 1228, 1932, 1565, 1605, 2249, 1982, 1908, 1945, 2680, 1810, 2182, 2187, 1657, 2165, 1894, 2188, 1724, 1664, 2329, 1886, 2076, 2078, 1844, 2044, 1856, 1369, 2246, 1966, 2066, 1853, 2217, 2149, 2305, 2184, 1769, 1537, 1587, 1739, 1471, 2221, 1649, 1946, 1818, 1863, 2681, 1672, 2408, 1674, 2650, 2763, 1989, 1314, 1747, 2104, 2482, 2383, 2011, 1863, 2087, 1603, 1964, 2381, 2101, 2459, 1855, 2232, 2100, 1834, 2063, 2447, 1655, 1558, 2159, 1738, 1791, 2487, 2396, 2557, 2740, 2066, 1854, 1949, 1831, 1906, 2148, 1670, 1975, 1566, 2362, 2251, 2375, 2100, 2350, 2035, 1888, 1639, 1871, 2333, 2269, 2700, 2234, 1784, 2609, 1871, 1959, 1493, 1762, 1962, 1962, 2172, 2665, 1931, 1862, 2080, 1863, 2285, 1730, 2650, 1761, 2112, 1880, 1726, 2082, 1522, 2233, 2481, 2281, 2470, 1526, 2664, 1870, 2044, 1927, 2385, 2238, 1732, 1635, 2062, 2343, 2305, 2103, 1884, 1829, 1797, 2082, 2212, 2543, 2215, 2149, 1686, 1787, 1559, 1558, 2153, 1429, 2298, 2007, 1762, 2051, 2048, 2067, 1945, 1609, 2383, 2206, 1715, 2159, 1733, 1677, 1798, 2239, 2173, 2127, 2160, 2396, 2167, 2500, 1901, 1357, 1886, 1787, 1681, 1899, 1775, 2357, 2298, 2078, 1828, 1813, 1977, 2565, 2436, 1791, 2271, 2070, 2231, 2310, 1912, 1834, 1925, 1882, 2325, 2130, 2178, 2245, 2126, 2337, 2083, 2350, 1732, 1622, 1396, 2157, 1755, 2281, 1720, 1719, 2549, 1564, 1825, 2072, 2326, 1918, 1874, 1563, 2326, 2421, 1556, 2373, 2232, 1983, 2282, 1861, 1949, 1946, 2018, 2067, 1417, 1771, 1720, 1887, 2320, 2269, 1762, 1525, 2653, 1994, 2174, 2183, 2153, 2200, 2082, 2125, 1819, 2377, 1809, 2115, 1850, 2473, 2325, 1457, 2093, 1705, 1960, 2261, 1929, 1709]
--- 56.27948474884033 seconds ---
"""