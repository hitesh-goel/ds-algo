def longest_subscring(str, k):
    ws = 0
    max_len = 0
    temp_len = 0
    temp = {}
    for we in range(len(str)):
        if temp.get(str[we], None):
            temp[str[we]] += 1
        else:
            temp[str[we]] = 1
        
        temp_len += 1
        print('we: ', we, 'ws: ', ws, 'temp: ', temp)
        while len(temp) > k:
            temp[str[ws]] -= 1
            if temp[str[ws]] == 0:
                temp.pop(str[ws])
            ws += 1
            temp_len -= 1
        
        max_len = max(max_len, temp_len)
    
    return max_len


def main():
    assert(longest_subscring("araaci", 2) == 4)
    assert(longest_subscring("araaci", 1) == 2)
    assert(longest_subscring("cbbebi", 3) == 5)

if __name__ == '__main__':
    main()
