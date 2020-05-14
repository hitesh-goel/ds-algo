# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
#
# Example 1:
#
# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
# Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
#
# Example 2:
#
# Input: L1=[5, 8, 9], L2=[1, 7]
# Output: [1, 5, 7, 8, 9]

from heapq import *


def k_merge(arr_list):
    m_arr, heap, l, j, counters = [], [], 0, 0, {}
    for i, arr in enumerate(arr_list):
        l += len(arr)
        heappush(heap, (arr[0], i))
        counters[i] = counters.get(i, 0) + 1

    while j < l:
        pop = heappop(heap)
        m_arr.append(pop[0])
        if counters[pop[1]] < len(arr_list[pop[1]]):
            heappush(heap, (arr_list[pop[1]][counters[pop[1]]], pop[1]))
            counters[pop[1]] += 1
        j += 1
    return m_arr


def main():
    assert k_merge([[2, 6, 8], [3, 6, 7], [1, 3, 4]]) == [1, 2, 3, 3, 4, 6, 6, 7, 8]
    assert k_merge([[5, 8, 9], [1, 7]]) == [1, 5, 7, 8, 9]
    pass


if __name__ == '__main__':
    main()