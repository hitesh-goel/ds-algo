def cyclic_sort(arr):
    k = 0
    while k < len(arr):
        if k+1 != arr[k]:
            i = arr[k]
            arr[k] = arr[i-1]
            arr[i-1] = i
        else:
            k += 1
            
    return arr

def main():
    assert(cyclic_sort([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5])
    assert(cyclic_sort([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6])
    assert(cyclic_sort([1, 5, 6, 4, 3, 2]) == [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    main()
