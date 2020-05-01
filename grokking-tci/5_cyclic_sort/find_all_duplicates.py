# 1, 4, 4, 3, 2
# 1, 2, 4, 3, 4
import time


def find_duplicate(arr):
    n = len(arr)
    i = 0
    duplicates = []
    while i < n:
        t = arr[i]
        if t != i+1:
            if arr[t-1] != t:
                arr[i], arr[t-1] = arr[t-1], arr[i]
            else:
                duplicates.append(t)
                i += 1
        else:
            i += 1
    print(arr)
    return duplicates


def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    print(nums)
    duplicate_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers


def main():
    print(find_duplicate([3, 4, 4, 5, 7, 7, 7]))
    print(find_duplicate([5, 4, 7, 2, 3, 5, 3]))
    pass


def main_2():
    print(find_all_duplicates([3, 4, 4, 5, 7, 7, 7]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
    pass


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    main_2()
    print("--- %s seconds ---" % (time.time() - start_time))
