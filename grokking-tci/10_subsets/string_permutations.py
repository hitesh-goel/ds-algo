# Given a string, find all of its permutations preserving the character sequence but changing case.
from collections import deque


def string_permutations(str_p):
    arr = deque()
    arr.append("")
    for i in range(len(str_p)):
        for j in range(len(arr)):
            temp = arr.popleft()
            if not str_p[i].isalpha():
                arr.append(temp + str_p[i])
            else:
                temp_1 = temp + str_p[i].lower()
                temp_2 = temp + str_p[i].upper()
                arr.append(temp_1)
                arr.append(temp_2)
    return list(arr)


def string_permutations_gtci(str_p):
    pms = [str_p]

    for i in range(len(str_p)):
        if str_p[i].isalpha():
            n = len(pms)
            for j in range(n):
                chs = list(pms[j])
                chs[i] = chs[i].swapcase()
                pms.append(''.join(chs))
    return pms


def main():
    print(string_permutations("ab7c"))
    print(string_permutations_gtci("ab7c"))
    pass


if __name__ == '__main__':
    main()