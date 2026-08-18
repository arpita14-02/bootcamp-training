class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        new_node= Node(data)
        new_node.next=self.head
        self.head=new_node