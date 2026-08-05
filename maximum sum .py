nums = [1,-2,3,-2]
total = nums[0]
curr_max = nums[0]
max_sum = nums[0]
curr_min = nums[0]
min_sum = nums[0]

for i in range(1, len(nums)):
            total += nums[i]

            
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

        
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

if max_sum < 0:
            ans = max_sum
else:
            ans = max(max_sum, total - min_sum)

print(ans)
   