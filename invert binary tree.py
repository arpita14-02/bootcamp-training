class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def invert(root):
    if root:
        root.left, root.right = invert(root.right), invert(root.left)
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root = invert(root)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

preorder(root)