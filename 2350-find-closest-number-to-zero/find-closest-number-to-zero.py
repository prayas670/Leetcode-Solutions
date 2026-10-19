class Solution:
    def findClosestNumber(self, nums):
        closest = nums[0]
        i = 1

        while i < len(nums):
            current = nums[i]

            current_dist = current
            closest_dist = closest

            if current_dist < 0:
                current_dist = -current_dist

            if closest_dist < 0:
                closest_dist = -closest_dist

            if current_dist < closest_dist:
                closest = current
            elif current_dist == closest_dist:
                if current > closest:
                    closest = current

            i += 1

        return closest