# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that
# the sum of all the node values of each path equals ‘S’.
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def seq_paths(root, seq):
    if root is None and len(seq) == 0:
        return True

    if root is None:
        return False

    if root.val == seq.pop(0):
        return seq_paths(root.left, list(seq)) or seq_paths(root.right, list(seq))
    else:
        return False


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    arr = []
    arr.extend([1, 0, 7])
    print("Tree has seq: " + str(seq_paths(root, arr)))


if __name__ == '__main__':
    main()
