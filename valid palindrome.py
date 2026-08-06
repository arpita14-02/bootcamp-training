s = input("Enter a string: ")

new = ""

for ch in s:
    if ch.isalnum():
        new += ch.lower()

left = 0
right = len(new) - 1

while left < right:
    if new[left] != new[right]:
        print(False)
        break
    left += 1
    right -= 1
else:
    print(True)