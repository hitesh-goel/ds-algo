# Given a binary tree, populate an array to represent its level-by-level traversal.
# You should populate the values of all nodes of each level from left to right in separate sub-arrays.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bt_level_order(root):
    queue = [root]
    result = []
    while len(queue) > 0:
        l = len(queue)
        temp = []
        while l > 0:
            el = queue.pop(0)
            temp.append(el.val)
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
            l -= 1
        result.append(temp)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(bt_level_order(root))


if __name__ == '__main__':
    main()
