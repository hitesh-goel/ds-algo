def happy_number(nos, n):
    t = n
    arr = []
    while t != 0:
        arr.append(t%10)
        t = int(t/10)
    s = 0
    for k in arr:
        s += k*k
    if s == 1:
        return True
    elif s in nos:
        return False
    else:
        nos.append(s)
        return happy_number(nos, s)

def main():
    assert(happy_number([], 23) == True)
    assert(happy_number([], 12) == False)

if __name__ == '__main__':
    main()

