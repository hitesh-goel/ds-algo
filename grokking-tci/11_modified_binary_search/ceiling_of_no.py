# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
# The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.


def get_ceiling(arr, key):
    s, e = 0, len(arr)-1

    if key < arr[s]:
        return s

    if key > arr[e]:
        return -1

    m = int(s + (e - s) / 2)

    while s < e:
        m = int(s + (e-s)/2)
        if arr[m] == key or arr[m-1] < key < arr[m]:
            return m
        if arr[m] < key < arr[m+1]:
            return m + 1
        if arr[m] < key:
            s = m + 1
        else:
            e = m - 1


def get_ceiling_gtci(arr, key):
    s, e = 0, len(arr) - 1

    if key > arr[e]:
        return -1

    while s < e:
        m = s + (e-s) // 2

        if arr[m] < key:
            s = m + 1
        elif arr[m] > key:
            e = m - 1
        else:
            return m

    return s

def main():
    print(get_ceiling_gtci([4, 6, 10], 6))
    print(get_ceiling_gtci([4, 6, 10], -1))
    print(get_ceiling_gtci([4, 6, 10], 17))
    print(get_ceiling_gtci([1, 3, 8, 10, 15], 12))


if __name__ == '__main__':
    main()