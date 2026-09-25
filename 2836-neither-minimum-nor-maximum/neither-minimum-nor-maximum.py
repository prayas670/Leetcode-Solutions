class Solution(object):
    def findNonMinOrMax(self, nums):
        n = len(nums)

        if n < 3:
            return -1

        a = nums[0]
        b = nums[1]
        c = nums[2]

        if (a <= b and b <= c) or (c <= b and b <= a):
            return b

        if (b <= a and a <= c) or (c <= a and a <= b):
            return a

        return c        
        