num = int(input())

while num >= 10:
    s = 0
    while num:
        s += num % 10
        num //= 10
    num = s

print(num)