class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def inorder_print(self, node, traversal):
        """Left -> Root -> Right"""
        if node:
            traversal = self.inorder_print(node.left, traversal)
            traversal += str(node.value) + " "
            traversal = self.inorder_print(node.right, traversal)

        return traversal

    def valid_bst(self, node):
        if node is None:
            return True

        if node.left:
            if node.left.value > node.value:
                return False
            if not self.valid_bst(node.left):
                return False

        if node.right:
            if node.right.value < node.value:
                return False
            if not self.valid_bst(node.right):
                return False

        return True


tree = BinaryTree(5)
tree.root.left = Node(2)
tree.root.right = Node(10)
tree.root.left.left = Node(1)
tree.root.left.right = Node(4)
tree.root.right.right = Node(3)

# print(tree.inorder_print(tree.root, ""))
print(tree.valid_bst(tree.root))