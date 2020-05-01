# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that
# the sum of all the node values of each path equals ‘S’.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_paths(root, s):
    if root is None:
        return

    s = s*10 + root.val

    if root.left is None and root.right is None:
        return s

    return all_paths(root.left, s) + all_paths(root.right, s)


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    arr = []
    print("Tree sum of paths: " + str(all_paths(root, 0)))


if __name__ == '__main__':
    main()
