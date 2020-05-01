# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

def missing_numbers(arr):
    i, n = 0, len(arr) 
    while i < n:
        t = arr[i]
        if t < n and t != i:
            arr[i], arr[t] = arr[t], arr[i]
        else:
            i += 1
    for k, val in enumerate(arr):
        if k != val:
            return k
    return 0

def main():
    assert(missing_numbers([4, 0, 3, 1]) == 2)
    assert(missing_numbers([8, 3, 5, 2, 4, 6, 0, 1]) == 7)

if __name__ == '__main__':
    main()
