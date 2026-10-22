class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        stack = []
        greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            if num in greater:
                result.append(greater[num])
            else:
                result.append(-1)

        return result