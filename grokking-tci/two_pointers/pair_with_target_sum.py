def find_pair(arr, k):
    p1, p2 = 0, len(arr)-1
    
    while p1 < p2:
        temp = arr[p1] + arr[p2]
        if temp > k:
            p2 -= 1
        elif temp < k:
            p1 += 1
        else:
            return [p1, p2]
    return []

def main():
    assert(find_pair([1, 2, 3, 4, 6], 6) == [1,3])
    assert(find_pair([2, 5, 9, 11], 11) == [0,2])

if __name__ == '__main__':
    main()
