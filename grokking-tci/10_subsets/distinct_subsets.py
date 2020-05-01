# Given a set with distinct elements, find all of its distinct subsets.


def distinct_subsets(arr):
    subsets = [[]]
    arr.sort()
    si, ei = 0, 0
    for j in range(len(arr)):
        si = 0
        if j != 0 and arr[j-1] == arr[j]:
            si = ei + 1
        ei = len(subsets) - 1
        for i in range(si, ei+1):
            temp = list(subsets[i])
            temp.append(arr[j])
            subsets.append(temp)

    return subsets


def main():
    print(distinct_subsets([1, 5, 3, 1]))
    pass


if __name__ == '__main__':
    main()