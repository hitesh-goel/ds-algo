def sqr(el):
    return el * el


# my first version without looking into solution
def squaring_arr(arr):
    i = 0
    temp = []
    while arr[i] <= 0:
        i += 1
    
    p1, p2 = i, i

    while p1 + p2 < len(arr):
        if sqr(arr[p2]) > sqr(arr[p1]) and p1 < len(arr):
            temp.append(sqr(arr[p1]))
            p1 += 1
        elif p2 >= 0:
            temp.append(sqr(arr[p2]))
            p2 -= 1
    return temp


# after looking into solution
def squaring_arr_2(arr):
    n = len(arr)
    res = [0]*n
    hn = n-1
    p1, p2 = 0, n-1
    while p1 <= p2:
        l = sqr(arr[p1])
        r = sqr(arr[p2])
        if l > r:
            res[hn] = l
            p1 += 1
        else:
            res[hn] = r
            p2 -= 1
        hn -= 1
    return res

def main():
    assert(squaring_arr_2([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9])
    assert(squaring_arr_2([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9])

if __name__ == '__main__':
    main()
