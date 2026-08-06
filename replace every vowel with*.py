s = input("Enter a string: ")

for v in "aeiouAEIOU":
    s = s.replace(v, "*")

print(s) 