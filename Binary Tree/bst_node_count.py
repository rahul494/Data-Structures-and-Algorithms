class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def size(self):

        def determine_size(node, size):
            if node:
                size += 1
                size = determine_size(node.left, size)
                size = determine_size(node.right, size)

            return size

        return determine_size(self.root, 0)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size())