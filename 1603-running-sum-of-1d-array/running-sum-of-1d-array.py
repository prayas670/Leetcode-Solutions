class Solution(object):
    def runningSum(self, nums):
        n = len(nums)

        ans = [0] * n

        total = 0
        
        i = 0

        while i < n:
            total = total + nums[i]
            ans[i] = total

            i += 1

        return ans    
        