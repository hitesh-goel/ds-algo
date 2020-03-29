def search_triplets(arr, target, left, triplets):
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] == target:
    pass

def closest_triplets(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_triplets(arr, target-arr[i], i+1, triplets)
    return triplets

def main():
    assert(closest_triplets([-3, -1, 1, 2], 1) == 0)
    pass

if __name__ == '__main__':
    main()
