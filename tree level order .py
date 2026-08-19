class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []

    q = [root]
    ans = []

    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans.append(level)

    return ans

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(levelOrder(root))