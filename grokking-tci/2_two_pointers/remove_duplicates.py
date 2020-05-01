#Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;

def remove_duplicates(arr):
    p1, p2 = 1, 1
    
    while p2 < len(arr):
        if arr[p1-1] != arr[p2]:
            arr[p1] = arr[p2]
            p1 += 1
        p2 += 1
    return p1

def main():
    assert(remove_duplicates([2, 3, 3, 3, 6, 9, 9]) == 4)
    assert(remove_duplicates([2, 2, 2, 2, 11]) == 2)

if __name__ == '__main__':
    main()
