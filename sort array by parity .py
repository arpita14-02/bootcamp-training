arr = [3, 1, 2, 4]

even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

ans = even + odd

print(ans)

