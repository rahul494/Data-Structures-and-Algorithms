class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if not root:
        return False

    # if the current node is a leaf and is equal to the sum, we've found a path
    if root.val == sum and not root.left and not root.right:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the recursive calls return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
