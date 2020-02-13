# Find a duplicate without using extra space


# Solution:
# - Calculate the length of List
# - Treat Last node as a Head of the Linked List
# - From Last element in List traverse and find the following.
# - Find a cycle in a list
# - Find the length of a cycle in a list
# - traverse the length to find the first element of the cycle
# - That element is the element with duplicates

def iterate_list(list, nos, index):
    t = nos
    newIndex = list[index] - 1
    while t > 1:
        newIndex = list[newIndex] - 1
        t -= 1
    return newIndex


def calculate_cycle_length(list, si):
    len = 0
    i = si
    while True:
        i = iterate_list(list, 1, i)
        len += 1
        if i == si:
            break
    return len


def calculate_duplicate_val(list, cl):
    si = len(list)-1
    ei = iterate_list(list, cl, len(list)-1)
    while si != ei:
        si = iterate_list(list, 1, si)
        ei = iterate_list(list, 1, ei)
    return si + 1


def main():
    list = [3, 1, 4, 2, 4, 5]
    list = [3, 4, 2, 3, 1, 5]
    list = [3, 1, 2, 2]
    list = [4, 3, 1, 1, 4]
    l = len(list)
    i = iterate_list(list, l-1, l-1)
    cl = calculate_cycle_length(list, i)
    pos = calculate_duplicate_val(list, cl)
    print('duplicate entry is ', pos)


def test():
    list = [3, 1, 4, 2, 4, 5]
    assert(iterate_list(list, 2, 5)) == 3
    assert(iterate_list(list, 4, 2)) == 2
    assert(calculate_cycle_length(list, 2)) == 4
    assert(calculate_duplicate_val(list, 4)) == 4


test()
main()
