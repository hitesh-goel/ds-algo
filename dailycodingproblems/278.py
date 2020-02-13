# return value of an element if that value is equal to it's index else return False

def element_exists(arr):
    for i,k in enumerate(arr):
        if i == k:
            return k
    return False

def main():
    arr1 = [1,2,2,3,5,6]
    arr2 = [1,2,3,4,5,6]
    assert(element_exists(arr1) == 2)
    assert(element_exists(arr2) == False)

if __name__ == '__main__':
    main()
