# Given an array of numbers sorted in ascending order,
# find the element in the array that has the minimum difference with the given ‘key’.
import math


def min_diff_key(arr, key):
    s, e = 0, len(arr) - 1

    if arr[s] >= key:
        return arr[s]
    if arr[e] <= key:
        return arr[e]

    while s <= e:
        m = s + (e-s)//2
        if arr[m] == key:
            return arr[m]
        elif arr[m] > key:
            e = m - 1
        else:
            s = m + 1

    if arr[s] - key < key - arr[e]:
        return arr[s]

    return arr[e]


def main():
    print(min_diff_key([4, 6, 10], 4))
    print(min_diff_key([4, 6, 10], 17))
    print(min_diff_key([1, 3, 8, 10, 15], 12))


if __name__ == '__main__':
    main()