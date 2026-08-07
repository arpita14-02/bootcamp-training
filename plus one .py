digits = [1,2,3]
n = len(digits)

for i in range(n - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        break
    digits[i] = 0
else:
    digits = [1] + digits

print(digits)