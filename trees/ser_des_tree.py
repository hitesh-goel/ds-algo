# serialise & deserialize a binary tree


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialise(self, str):
        if self == None:
            str.append(-1)
            return
        str.append(self.val)
        if self.left != None:
            self.left.serialise(str)
        else:
            str.append(-1)
        if self.right != None:
            self.right.serialise(str)
        else:
            str.append(-1)

    def deserialize(str):
        node = Node(str.val)
        return


def main():
    n = Node(5)
    n1 = Node(3)
    n.left = n1
    str_arr = []
    n.serialise(str_arr)
    print(str_arr)


main()
