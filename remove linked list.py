head = [1,2,6,3,4,5,6]
val = 6
while head and head.val == val:
            head = head.next

cur = head
while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

print(head)