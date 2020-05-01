# without using * for multiply
# use recursion to multiply 2 integers
# [IMPROVEMENT] add twice the no's
import math
hm = {}


def multiply(a, b):
    if a > b:
        t = b
        b = a
        a = t
    if a == 0:
        return 0
    if a == 1:
        return b

    fl = math.floor(a/2)
    cl = math.ceil(a/2)

    fkey = "{0}-{1}".format(fl, b)
    if fkey in hm:
        fm = hm[fkey]
    else:
        fm = multiply(fl, b)
        hm[fkey] = fm

    lkey = "{0}-{1}".format(cl, b)
    if lkey in hm:
        lm = hm[lkey]
    else:
        lm = multiply(cl, b)
        hm[lkey] = lm

    return fm + lm


def test():
    assert(multiply(1110, 1210) == 1110*1210)
    print(hm)


test()
