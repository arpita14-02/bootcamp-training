s = input("Enter a string: ")

i = 0
n = len(s)

# Skip leading spaces
while i < n and s[i] == " ":
    i += 1

sign = 1
if i < n and (s[i] == "+" or s[i] == "-"):
    if s[i] == "-":
        sign = -1
    i += 1

num = 0

while i < n and s[i].isdigit():
    num = num * 10 + int(s[i])
    i += 1

num = num * sign

if num < -2**31:
    num = -2**31
elif num > 2**31 - 1:
    num = 2**31 - 1

print(num)