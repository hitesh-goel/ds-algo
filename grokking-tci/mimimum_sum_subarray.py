# get the minimum sum of subarrays size of k

def get_minimum(arr, k):
    max_sum = 0
    temp_sum = 0
    for i in range(len(arr)):
        temp_sum += arr[i]
        if i  >= k-1:
            max_sum = max(max_sum, temp_sum)
            temp_sum -= arr[i-k]
    return max_sum 

def main():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    sum = get_minimum(arr, k)
    assert(sum == 9)

if __name__ == '__main__':
    main()
