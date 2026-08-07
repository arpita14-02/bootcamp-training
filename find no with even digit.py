nums = [12,345,2,6,7896]
nums = list(map(int, input().split()))

count = 0
for num in nums:
    if len(str(num)) % 2 == 0:
        count += 1

print(count)