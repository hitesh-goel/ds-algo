# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values
# of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the
# same manner for the following levels.
import time
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root):
    queue = deque()
    queue.append(root)
    result = []
    switch = True
    while len(queue) > 0:
        l = len(queue)
        temp = deque()
        while l > 0:
            el = queue.popleft()

            if switch:
                temp.append(el.val)
            else:
                temp.appendleft(el.val)

            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
            l -= 1
        switch = not switch
        result.append(list(temp))
    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    start_time = time.time()
    print(zig_zag_traversal(root))
    print("--- %s seconds ---" % (time.time() - start_time))
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    start_time = time.time()
    print(zig_zag_traversal(root))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
