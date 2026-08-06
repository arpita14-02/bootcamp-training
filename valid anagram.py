s = input("Enter first string: ")
t = input("Enter second string: ")

if len(s) != len(t):
    print(False)
else:
    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in t:
        if ch not in count:
            print(False)
            break
        count[ch] -= 1
        if count[ch] < 0:
            print(False)
            break
    else:
        print(True)