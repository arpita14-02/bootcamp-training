nums = [2, 7, 11, 15]
target = 9

mp = {}

for i in range(len(nums)):
    req = target - nums[i]

    if req in mp:
        print([mp[req], i])
        break

    mp[nums[i]] = i