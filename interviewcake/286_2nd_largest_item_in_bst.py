# https://www.interviewcake.com/question/python3/second-largest-item-in-bst


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def second_largest_el(root):
    temp = root
    last = root
    while temp.right is not None:
        if temp.right.right is None:
            last = temp
        temp = temp.right

    if temp.left is not None:
        temp = temp.left
        while temp is not None:
            last = temp
            temp = temp.right

    return last.value


def main():
    root = BinaryTreeNode(50)
    t_17 = root.insert_left(17)
    t_23 = t_17.insert_right(23)
    t_23.insert_left(19)
    t_72 = root.insert_right(72)
    t_54 = t_72.insert_left(54)
    t_54.insert_right(67)
    t_12 = t_17.insert_left(12)
    t_12.insert_left(9)
    t_12.insert_right(14)
    assert second_largest_el(root) == 67
    t_72.insert_right(76)
    assert second_largest_el(root) == 72
    pass


if __name__ == '__main__':
    main()