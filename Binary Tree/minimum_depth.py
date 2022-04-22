from collections import deque
import queue

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_minimum_depth(root):
    if not root:
        return 0
    
    queue = deque()
    queue.append(root)
    minimumTreeDepth = 0

    while queue:
        minimumTreeDepth += 1
        levelSize = len(queue)

        for _ in range(levelSize):
            curr = queue.popleft()

            if not curr.left and not curr.right:
                return minimumTreeDepth

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))

main()