# Design a class to efficiently find the Kth largest element in a stream of numbers.
#
# The class should have the following two things:
#
# The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
# The class should expose a function add(int num) which will store the given number and return the Kth largest number.
#
# Example 1:
#
# Input: [3, 1, 5, 12, 2, 11], K = 4
# 1. Calling add(6) should return '5'.
# 2. Calling add(13) should return '6'.
# 2. Calling add(4) should still return '6'.


from heapq import *


class KLargestInStream:
    def __init__(self, arr, k):
        self.stream = []
        for i, no in enumerate(arr):
            if i < k:
                heappush(self.stream, no)
            elif self.stream[0] < no:
                    heappop(self.stream)
                    heappush(self.stream, no)

        pass

    def add(self, no):
        heappush(self.stream, no)
        heappop(self.stream)
        return self.stream[0]


def k_largest_stream():
    stream = KLargestInStream([3, 1, 5, 12, 2, 11], 4) # [3, 5, 11, 12]
    assert stream.add(6) == 5
    assert stream.add(13) == 6
    assert stream.add(4) == 6
    pass


def main():
    k_largest_stream()
    pass


if __name__ == '__main__':
    main()
