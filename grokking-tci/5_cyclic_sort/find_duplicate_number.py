# 1, 4, 4, 3, 2
# 1, 2, 4, 3, 4
import time


def find_duplicate(arr):
    n = len(arr)
    i = 0
    while i < n:
        t = arr[i]
        if arr[i] != i+1:
            if arr[t-1] != t:
                arr[i], arr[t-1] = arr[t-1], arr[i]
            else:
                return t
        else:
            i += 1
    return -1


def main():
    assert(find_duplicate([1, 4, 4, 3, 2]) == 4)
    assert(find_duplicate([2, 1, 3, 3, 5, 4]) == 3)
    assert(find_duplicate([2, 4, 1, 4, 4]) == 4)
    pass


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
