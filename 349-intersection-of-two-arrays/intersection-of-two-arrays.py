class Solution:
    def intersection(self, nums1, nums2):
        result = []

        for i in range(len(nums1)):
            found = False

            for j in range(len(result)):
                if result[j] == nums1[i]:
                    found = True
                    break

            if found:
                continue

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    result.append(nums1[i])
                    break

        return result                            