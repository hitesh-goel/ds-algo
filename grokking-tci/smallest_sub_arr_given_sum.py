# get length of smallest sub arr whose sum is >= s
import math

def get_sm_arr(arr, s):
    sum = 0
    sl = math.inf
    ws = 0
    for we in range(len(arr)):
        sum += arr[we]
        while sum >= s:
            sl = min(sl, we - ws + 1)
            sum -= arr[ws]
            ws += 1
    return sl

def main():
    assert(get_sm_arr([2, 1, 5, 2, 3, 2], 7) == 2)
    assert(get_sm_arr([2, 1, 5, 2, 8], 7) == 1)
    assert(get_sm_arr([3, 4, 1, 1, 6], 8) == 3)
 
if __name__ == '__main__':
    main()
