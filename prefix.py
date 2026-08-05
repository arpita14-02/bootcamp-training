arr=[1,3,7,11,13,2,5]
for i in range(1,len(arr)):
   arr[i]=arr[i]+arr[i-1]
   print(arr)


