head = [1,2,3,4,5]
p = None
while head:
            temp = head
            head = head.next
            temp.next = p
            p = temp
print(p)