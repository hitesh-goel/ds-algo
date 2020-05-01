def main():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    win_sum, win_start, arr_avg = 0, 0, []

    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        if win_end >= k-1:
            arr_avg.append(win_sum/k)
            win_sum -= arr[win_start]
            win_start += 1
    
    return arr_avg
    
    
    return avg_arr 

if __name__ == '__main__':
    print(main())
