# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
# Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.
#
# Example 1:
# Input: [5, 6, 7, 8, 9], K = 3, X = 7
# Output: [6, 7, 8]
#
# Example 2:
# Input: [2, 4, 5, 6, 9], K = 3, X = 6
# Output: [4, 5, 6]
#
# Example 3:
# Input: [2, 4, 5, 6, 9], K = 3, X = 10
# Output: [5, 6, 9]


from heapq import *


def k_closest(arr, k, x):
    # store the diff of each element of arr to x
    # get the top min elements
    heap = []
    for i, no in enumerate(arr):
        abs_no = abs(x - no)
        if i < k:
            heappush(heap, (-abs_no, no))
        elif abs_no < -heap[0][0]:
            heappop(heap)
            heappush(heap, (-abs_no, no))

    return [a[1] for a in heap]


def main():
    assert k_closest([2, 4, 5, 6, 9], 3, 6) == [4, 5, 6]
    assert k_closest([2, 4, 5, 6, 9], 3, 10) == [5, 6, 9]
    assert k_closest([5, 6, 7, 8, 9], 3, 7) == [6, 7, 8]
    pass


if __name__ == '__main__':
    main()
