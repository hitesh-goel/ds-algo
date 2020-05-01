# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

from heapq import *
from heapq import _siftup, _siftdown


class MedianOfStream:
    min_heap = []
    max_heap = []

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] > num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        self.rebalance()

    def remove(self, heap, el):
        ind = heap.index(el)  # find the element
        # move the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if ind < len(heap):
            _siftup(heap, ind)
            _siftdown(heap, 0, ind)

    def pop_number(self, el):
        if el <= -self.max_heap[0]:
            self.remove(self.max_heap, -el)
        else:
            self.remove(self.min_heap, el)
        self.rebalance()

    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0]/2.0 + self.min_heap[0]/2.0
        else:
            return -self.max_heap[0]/1.0


def main():
    k = 2
    arr = [1, 2, -1, 3, 5]

    j = 0
    med_arr = []
    median_of_stream = MedianOfStream()

    while j < k-1:
        median_of_stream.insert_num(arr[j])
        j += 1

    i = 0
    while j < len(arr):
        median_of_stream.insert_num(arr[j])
        med_arr.append(median_of_stream.find_median())
        median_of_stream.pop_number(arr[i])
        j += 1
        i += 1

    print("The median of window: ", med_arr)


if __name__ == '__main__':
    main()
