# find all subsets of a set


def subsets_of_set(set_val):
    arr_sets = []
    if len(set_val) == 1:
        arr_sets.append(set_val)
    else:
        el = set_val.pop()
        temp_set = set()
        temp_set.add(el)
        arr_sets.append(temp_set)
        ns = set_val.copy()
        sets = subsets_of_set(ns)
        for ss in sets:
            temp = ss.copy()
            temp.add(el)
            arr_sets.append(temp)
            arr_sets.append(ss)
    return arr_sets


def test():
    temp = set()
    temp.add(1)
    temp.add(2)
    temp.add(3)
    temp.add(4)
    print(subsets_of_set(temp))


test()
