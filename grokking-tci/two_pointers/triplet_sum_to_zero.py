def get_triplets(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
        elif arr[left] + arr[right] > target_sum:
            right -= 1
        else:
            left += 1

def triplet_sum_to_zero(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        get_triplets(arr, -arr[i], i+1, triplets)
    return triplets

def main():
    assert(triplet_sum_to_zero([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]])

if __name__ == '__main__':
    main()
