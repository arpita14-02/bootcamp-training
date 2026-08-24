class Solution:
    def permute(self, nums):
        ans = []

        def backtrack(current):
            if len(current) == len(nums):
                ans.append(current.copy())
                return

            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()

        backtrack([])
        return ans


nums = [1, 2, 3]

obj = Solution()
print(obj.permute(nums))