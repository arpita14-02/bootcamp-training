nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3]

ans = []

for x in nums1:
    if x in nums2 and x not in ans:
        ans.append(x)

print(ans)