# find a node in order successor of a given node


class Node:
    def __init__(self, data):
        self.val = data
        self.l = None
        self.r = None
        self.p = None


def find_node(tree, val):
    if tree.val == val:
        return tree
    if tree.val < val and tree.r:
        return find_node(tree.r, val)
    elif tree.l:
        return find_node(tree.l, val)

    return None


def find_min_node(node):
    if node.l != None:
        return find_min_node(node.l)
    return node


def ios(root, val):
    node = find_node(root, val)
    if node.r == None:
        return node.p
    else:
        return find_min_node(node.r)


def test():
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(7)
    n4 = Node(9)
    n5 = Node(10)
    n6 = Node(11)
    n7 = Node(13)

    n1.p = n2

    n2.l = n1
    n2.r = n4
    n2.p = n5

    n3.p = n4

    n4.p = n2
    n4.l = n3

    n5.l = n2
    n5.r = n7

    n6.p = n7

    n7.p = n5
    n7.l = n6

    s = ios(n5, 5)
    assert(s.val == 7)


test()
