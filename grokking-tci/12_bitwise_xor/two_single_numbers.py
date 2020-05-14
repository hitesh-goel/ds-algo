# In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once.
# Find the two numbers that appear only once.


def find_two_single_number(arr):
    # get the xor of all of the numbers
    n1xn2 = arr[0]
    for i in range(1, len(arr)):
        n1xn2 = n1xn2 ^ arr[i]

    rmb = 1
    while (rmb & n1xn2) == 0:
        rmb = rmb << 1

    n1, n2 = 0, 0
    for no in arr:
        if (no & rmb) == 0:
            n1 ^= no
        else:
            n2 ^= no

    return [n1, n2]


def main():
    print(find_two_single_number([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    pass


if __name__ == '__main__':
    main()