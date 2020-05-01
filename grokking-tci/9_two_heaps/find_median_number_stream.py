from heapq import *


class MedianOfStream:
    min_heap = []
    max_heap = []

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] > num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

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
    median_of_stream = MedianOfStream()
    median_of_stream.insert_num(3)
    median_of_stream.insert_num(1)
    print("The median is: " + str(median_of_stream.find_median()))
    median_of_stream.insert_num(5)
    print("The median is: " + str(median_of_stream.find_median()))
    median_of_stream.insert_num(4)
    print("The median is: " + str(median_of_stream.find_median()))


if __name__ == '__main__':
    main()
