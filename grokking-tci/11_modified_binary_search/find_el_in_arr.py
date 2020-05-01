# Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
# Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
# You should assume that the array can have duplicates.
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.


def find_key(arr, l, r, k):
    if l > r:
        return -1

    m = int((l + r) / 2)

    if arr[m] == k:
        return m

    elif arr[m] > k:
        return find_key(arr, l, m - 1, k)
    else:
        return find_key(arr, m + 1, r, k)


def find_key_gtci(arr, k):
    s = 0
    e = len(arr) - 1

    is_aschending = arr[s] < arr[e]

    while s <= e:
        m = int(s + (e-s)/2)
        if arr[m] == k:
            return m
        elif arr[m] > k:
            if is_aschending:
                e = m - 1
            else:
                s = m + 1
        else:
            if is_aschending:
                s = m + 1
            else:
                e = m - 1
    return -1


def main():
    arr = [10, 6, 4]
    r = len(arr) - 1
    l = 0
    print(find_key_gtci(arr, 10))
    pass


if __name__ == '__main__':
    main()