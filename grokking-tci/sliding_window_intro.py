def main():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    sum = 0
    
    for i in range(k):
        sum = sum + arr[i]
    
    avg_arr = []

    for i in range(k, len(arr) + 1):
        temp = sum/k
        avg_arr.append(temp)
        if i < len(arr):
            sum = sum + arr[i] - arr[i-k]
    
    return avg_arr 

if __name__ == '__main__':
    print(main())
