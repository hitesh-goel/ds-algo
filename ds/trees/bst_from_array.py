# construct a BST from a sorted array
import math


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def create_sub_tree(arr):
    if not arr:
        return None
    mid = math.floor(len(arr)/2)
    root = Node(arr[mid])
    root.left = create_sub_tree(arr[:mid])
    root.right = create_sub_tree(arr[mid:])
    return root
