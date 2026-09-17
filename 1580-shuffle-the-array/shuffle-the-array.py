class Solution(object):
    def shuffle(self, nums, n):
        result = []

        i = 0
        
        while i < n:
            result.append(nums[i])
            result.append(nums[i + n])
            i += 1

        return result    
        