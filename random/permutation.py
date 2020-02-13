# calculate permutations of a string
import copy


def permutate(str):
    perm = []
    if len(str) == 0:
        perm.append([])
    else:
        fc = str[0]
        str_perms = permutate(str[1:])
        for p in str_perms:
            for j in range(0, len(p)+1):
                r = copy.deepcopy(p)
                r.insert(j, fc)
                perm.append(r)
    return perm


print(permutate('ab'))
assert(permutate('ab') == ['ab', 'ba'])
