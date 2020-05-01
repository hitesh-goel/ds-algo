# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that
# the sum of all the node values of that path equals ‘S’.
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, s):
    if s == 0 and root is None:
        return True

    if root is None:
        return False

    s = s - root.val
    return has_path(root.left, s) or has_path(root.right, s)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


if __name__ == '__main__':
    main()
