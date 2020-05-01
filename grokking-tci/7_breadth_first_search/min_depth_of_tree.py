# Find the minimum depth of a binary tree.
# The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
import time
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    depth = 1
    while len(queue) > 0:
        l = len(queue)
        while l > 0:
            el = queue.popleft()
            if not el.left and not el.right:
                return depth
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
            l -= 1
        depth += 1
    return depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(min_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(min_depth(root)))


if __name__ == '__main__':
    main()
