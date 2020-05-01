import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if len(self.arr) < index:
            return math.inf
        return self.arr[index]


def search_inf_arr(arr_reader, key):
    s, e = 0, 1
    while arr_reader.get(e) <= key:
        ns = e + 1
        e += (e - s + 1)*2
        s = ns

    while s <= e:
        m = s + (e - s) // 2
        if arr_reader.get(m) == key:
            return m
        elif arr_reader.get(m) < key:
            s = m + 1
        else:
            e = m - 1
    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_inf_arr(reader, 16))
    print(search_inf_arr(reader, 11))
    pass


if __name__ == '__main__':
    main()