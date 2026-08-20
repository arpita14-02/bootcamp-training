class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root