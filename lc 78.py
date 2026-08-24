class Solution:
    def subsets(self, nums):
        ans = []

        def backtrack(index, current):
            if index == len(nums):
                ans.append(current.copy())
                return

            
            backtrack(index + 1, current)

            
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()

        backtrack(0, [])
        return ans


nums = [1, 2, 3]

obj = Solution()
print(obj.subsets(nums))