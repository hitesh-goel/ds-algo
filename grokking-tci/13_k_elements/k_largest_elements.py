# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
from heapq import heappop, heappush


def k_largest_elms(arr, k):
    temp = []

    for el in arr:
        heappush(temp, -el)
    result = []

    while k > 0:
        result.append(-heappop(temp))
        k -= 1
    return result


def k_largest_elms_gtci(arr, k):
    temp = []
    s, e = 0, len(arr)

    while s < k:
        heappush(temp, arr[s])
        s += 1

    while s < e:
        if temp[0] < arr[s]:
            heappop(temp)
            heappush(temp, arr[s])
        s += 1

    return temp


def main():
    print(k_largest_elms([3, 1, 5, 12, 2, 11], 3))
    print(k_largest_elms_gtci([3, 1, 5, 12, 2, 11], 3))
    pass


if __name__ == '__main__':
    main()