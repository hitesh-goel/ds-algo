# Given a set of distinct numbers, find all of its permutations.
from collections import deque


def permutations(arr):
    pms = deque()
    pms.append([])
    for i in arr:
        for j in range(len(pms)):
            prev = pms.popleft()
            for k in range(len(prev)+1):
                temp = list(prev)
                temp.insert(k, i)
                pms.append(temp)
    return list(pms)


def rec_permutations(arr, i, cp, res):
    if i == len(arr):
        res.append(cp)
    else:
        for j in range(len(cp)+1):
            np = list(cp)
            np.insert(j, arr[i])
            rec_permutations(arr, i+1, np, res)


def main():
    print(permutations([1, 3, 5]))
    res = []
    rec_permutations([1, 3, 5], 0, [], res)
    print(res)


if __name__ == '__main__':
    main()
