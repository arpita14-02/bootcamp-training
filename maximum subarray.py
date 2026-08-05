nums = [-2,1,-3,4,-1,2,1,-5,4]
maxValue = nums[0]
sum = 0
for v in nums:
    sum += v
maxValue = max(maxValue, sum)
if sum < 0:
                sum = 0
print(maxValue)