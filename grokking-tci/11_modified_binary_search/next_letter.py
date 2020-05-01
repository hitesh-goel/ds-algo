# Given an array of lowercase letters sorted in ascending order,
# find the smallest letter in the given array greater than a given ‘key’.

# Assume the given array is a circular list,
# which means that the last letter is assumed to be connected with the first letter.
# This also means that the smallest letter in the given array is greater than the last letter of the array and is
# also the first letter of the array.


def get_next_letter(arr, key):
    s, e = 0, len(arr) - 1

    if key >= arr[e]:
        return s

    while s <= e:
        m = int(s + (e-s)/2)
        if arr[m] == key:
            return m + 1

        if arr[m] > key:
            e = m - 1
        else:
            s = m + 1

    return s


def main():
    print(get_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(get_next_letter(['b', 'c', 'f', 'h'], 'a'))
    print(get_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(get_next_letter(['a', 'c', 'f', 'h'], 'h'))
    pass


if __name__ == '__main__':
    main()