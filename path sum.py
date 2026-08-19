class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def hasPathSum(root, target):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target

    return (hasPathSum(root.left, target - root.val) or
            hasPathSum(root.right, target - root.val))

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)

print(hasPathSum(root, 20))