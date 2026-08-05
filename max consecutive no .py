nums = [1,1,0,1,1,1]
n = len(nums)
maxi = 0
count = 0
for i in range(0,n):
            if nums[i]== 1:
                count+=1
            else:
                count=0
            maxi= max(maxi,count)
print(maxi)

        