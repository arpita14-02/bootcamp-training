nums = [4, 2, 5, 7]

even = []
odd = []

for x in nums:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

ans = []

for i in range(len(nums)):
    if i % 2 == 0:
        ans.append(even.pop())
    else:
        ans.append(odd.pop())

print(ans)