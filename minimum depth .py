class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def minDepth(root):
    if not root:
        return 0

    if not root.left:
        return 1 + minDepth(root.right)

    if not root.right:
        return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(minDepth(root))