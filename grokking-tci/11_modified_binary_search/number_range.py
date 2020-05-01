# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’
# will be the first and last position of the ‘key’ in the array.
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
import math


def binary_search(arr, key, end_index):
    s, e = 0, len(arr) - 1
    id = -1

    while s < e:
        m = s + (e-s)//2

        if arr[m] < key:
            s = m + 1
        elif arr[m] > key:
            e = m - 1
        else:
            id = m
            if end_index:
                s = m + 1
            else:
                e = m - 1
    return id


def number_range_gtci(arr, key):
    result = [-1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)

    return result


def number_range(arr, key):
    s, e = 0, len(arr) - 1
    si, ei = math.inf, -1
    while s < e:
        m = int(s + (e-s)/2)
        if arr[m] == key:
            ms, me = m, m

            while ms >= s and arr[ms] == key:
                si = min(si, ms)
                ms = ms - 1
            while me <= e and arr[me] == key:
                ei = max(ei, me)
                me = me + 1
            return [si, ei]

        if arr[m] < key:
            s = m + 1
        elif arr[m] > key:
            e = m - 1

    return [-1, -1]


def main():
    print(number_range_gtci([4, 6, 6, 6, 9], 6))
    print(number_range_gtci([1, 3, 8, 10, 15], 10))
    print(number_range_gtci([1, 3, 8, 10, 15], 12))
    pass


if __name__ == '__main__':
    main()