s = "abciiidef", k = 3
left = 0
count = 0
ans = 0
window_size = 0
for right in range(0,len(s)):
            if s[right] in "aeiou":
                count += 1
            if (right - left +1) == k:
                ans = max(ans,count)
                if s[left] in "aeiou":
                    count -= 1
                left += 1
print(ans)
