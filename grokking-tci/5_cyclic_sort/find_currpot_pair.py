# 1, 4, 4, 3, 2
# 1, 2, 4, 3, 4
import time


def find_duplicate(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = arr[i] - 1
        if i != j and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for k, v in enumerate(arr):
        if k+1 != v:
            return [k+1, v]
    return -1


def main():
    assert(find_duplicate([3, 1, 2, 5, 2]) == [4, 2])
    assert(find_duplicate([3, 1, 2, 3, 6, 4]) == [5, 3])


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
