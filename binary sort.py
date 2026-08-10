arr =[3,5,8,1,2]
n= len(arr)
arr.sort()
x = 5
l = 0
r = n-1
while l <= r:
    m = (l+r)//2
    if arr[m] == x:
        print("arr")
        break
    elif arr[m] < x:
        l = m+1
    else:
        r = m-1
else:
    print("No")