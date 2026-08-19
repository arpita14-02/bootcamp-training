class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(maxDepth(root))