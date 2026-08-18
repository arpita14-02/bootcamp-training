head = [1,2,3,4,5]
slow = fast = head

while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

print(slow)