# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e.,
# the lowest level comes first.
from collections import deque
import time


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def bt_level_order(root):
#     queue = [root]
#     result = []
#     while len(queue) > 0:
#         l = len(queue)
#         temp = []
#         while l > 0:
#             el = queue.pop(0)
#             temp.append(el.val)
#             if el.left:
#                 queue.append(el.left)
#             if el.right:
#                 queue.append(el.right)
#             l -= 1
#         result.append(temp)
#     return result


def get_queue_items(queue_1, result):
    l = len(queue_1)
    if l == 0:
        return
    temp = []
    while l > 0:
        el = queue_1.popleft()
        temp.append(el.val)
        if el.left:
            queue_1.append(el.left)
        if el.right:
            queue_1.append(el.right)
        l -= 1
    get_queue_items(queue_1, result)
    result.append(temp)


def bt_level_order(root):
    queue_1 = deque()
    queue_1.append(root)
    result = []
    get_queue_items(queue_1, result)
    return result


def bt_level_order_2(root):
    queue_1 = deque()
    queue_2 = deque()
    queue_3 = deque()
    queue_1.append(root)
    result = []
    while len(queue_1) > 0:
        l = len(queue_1)
        queue_3.append(l)
        while l > 0:
            el = queue_1.popleft()
            queue_2.append(el)
            if el.right:
                queue_1.append(el.right)
            if el.left:
                queue_1.append(el.left)
            l -= 1

    while len(queue_2) > 0:
        l = queue_3.pop()
        temp = []
        while l > 0:
            el = queue_2.pop()
            temp.append(el.val)
            l -= 1
        result.append(temp)

    return result


def traverse(root):
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.appendleft(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    start_time = time.time()
    print(bt_level_order(root))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(bt_level_order_2(root))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(traverse(root))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
