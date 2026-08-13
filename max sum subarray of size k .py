arr = [100, 200, 300, 400]
k = 2
left = 0
window_sum = 0
ans = float('-inf')
for right in range(len(arr)):
    window_sum += arr[right]
    if right - left + 1 == k:
        ans = max(ans, window_sum)
        window_sum -= arr[left]
        left += 1
print(ans)