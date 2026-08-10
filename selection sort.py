arr =[3,8,1,5,2]
n = len(arr)
for i in range(0,n-2):
    min_index =1
    for j in range(i+1,n-1):
        if arr[j]<arr [min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
print(arr)
