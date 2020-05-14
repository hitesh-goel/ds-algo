# In a non-empty array of integers, every number appears twice except for one, find that single number.


def find_single_number(arr):
    no = arr[0]
    for i in range(1, len(arr)):
        no = no ^ arr[i]
    return no


def main():
    assert(find_single_number([1, 4, 2, 1, 3, 2, 3]) == 4)
    pass


if __name__ == '__main__':
    main()