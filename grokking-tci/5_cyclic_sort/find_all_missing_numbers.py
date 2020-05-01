
def find_all_missing_numbers(arr):
    i, n = 0, len(arr) 
    while i < n:
        t = arr[i]
        if t-1 != i and arr[i] != arr[t-1]:
            arr[i], arr[t-1] = arr[t-1], arr[i]
        else:
            i += 1
    nos = []
    for k, val in enumerate(arr):
        if k != val-1:
            nos.append(k+1)
    return nos

def main():
    print(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_all_missing_numbers([2, 4, 1, 2]))
    print(find_all_missing_numbers([2, 3, 2, 1]))

if __name__ == '__main__':
    main()
