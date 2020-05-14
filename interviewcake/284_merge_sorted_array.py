# https://www.interviewcake.com/question/python3/merge-sorted-arrays


def merge_arrays(a1, a2):
    l1, l2 = len(a1), len(a2)

    if l1 == 0 or l2 == 0:
        return a1 + a2

    m_arr = [None]*(l1+l2)
    t, i, j = 0, 0, 0

    while t < (l1+l2):
        if i < l1 and j < l2 and a1[i] < a2[j]:
            m_arr[t] = a1[i]
            i += 1
        else:
            m_arr[t] = a2[j]
            j += 1
        t += 1

    return m_arr


def main():
    print(merge_arrays([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))
    print(merge_arrays([3], [1, 5, 8, 12, 14, 19]))
    pass


if __name__ == '__main__':
    main()