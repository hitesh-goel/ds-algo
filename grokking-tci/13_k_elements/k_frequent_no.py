# Problem Statement #
#
# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
#
# Example 1:
#
# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.
#
# Example 2:
#
# Input: [5, 12, 11, 3, 11], K = 2
# Output: [11, 5] or [11, 12] or [11, 3]
# Explanation: Only '11' appeared twice, all other numbers appeared once.
from heapq import *


def k_freq_no(arr, k):
    d = {}

    for n in arr:
        d[n] = d.get(n, 0) + 1

    m = []
    for i, n in d.items():
        heappush(m, (n, i))
        if len(m) > k:
            heappop(m)

    el = []
    while len(m) > 0:
        el.append(heappop(m)[1])
    return el


def main():
    print(k_freq_no([1, 3, 5, 12, 11, 12, 11], 2))
    print(k_freq_no([5, 12, 11, 3, 11], 2))
    pass


if __name__ == '__main__':
    main()
