# if given tree is binary search tree


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def is_bst(root, min, max):
    ln = None
    rn = None
    isLBst = True
    isRBst = True

    if (max != None and max < root.val) or (min != None and root.val < min):
        return False

    if root.left != None:
        ln = root.left
        isLBst = is_bst(ln, min, root.val)
    if root.right != None:
        rn = root.right
        isRBst = is_bst(rn, root.val, max)

    return isLBst and isRBst


def test():
    n = Node(5)
    n1 = Node(3)
    n2 = Node(6)
    n3 = Node(7)

    n.left = n1
    n.right = n2
    n2.right = n3
    assert(is_bst(n, None, None)) == False


test()
