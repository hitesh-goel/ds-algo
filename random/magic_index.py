# A[0---n-1]
# Magic Index @ A[i] = i
# all integers are distinct
# array is sorted


def get_magic_index(arr):
    i = 0
    for item in arr:
        if i == item:
            return true
        i += 1
    return false


"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""


# if values are distinct and sorted arr[i] < i+1 get if magic index exist
# consider values can be negative as well.
def get_magic_index_2(arr):
    if 0 == arr[0]:
        return True
    return False


"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 2, 3, 5, 7, 8, 8, 8, 11, 12]
[1, 2, 3, 4, 6, 6, 7, 7, 8]
"""


# if values are not distinct but sorted check if magic index exist
# consider values can be negative as well.
# Also we can use min value out of midIndex or midValue to directly reduce no of elements as well.
def get_magic_index_3(arr, i, j):
    if j-1 < arr[0] or arr[j-i-1] < i:
        return False
    l = j - i
    if l == 1:
        return arr[0] == i

    nj = (i+j)//2
    return get_magic_index_3(arr[:l//2], i, nj) or get_magic_index_3(arr[l//2:], nj, j)


def test():
    arr = [1, 2, 3, 4, 6, 6, 6, 7, 8]
    arr = [1, 2, 3, 4, 6, 6, 7, 8, 9]
    assert(get_magic_index_3(arr, 0, len(arr))) == False


test()
