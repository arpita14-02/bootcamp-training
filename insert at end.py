class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
new = Node(40)
temp = head
while temp.next:
    temp = temp.next
temp.next = new
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next