# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that
# the sum of all the node values of each path equals ‘S’.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_paths(root, s, current_path, paths):
    if root is None:
        return

    current_path.append(root.val)

    if root.val == s and root.left is None and root.right is None:
        paths.append(list(current_path))

    s = s - root.val
    if root.left:
        all_paths(root.left, s, current_path, paths)
    if root.right:
        all_paths(root.right, s, current_path, paths)

    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    paths = []
    print("Tree has path: " + str(all_paths(root, 23, [], paths)))
    print(paths)


if __name__ == '__main__':
    main()
