class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in freq:
            count = freq[num]
            buckets[count].append(num)

        result = []

        i = len(nums)
        while i >= 1 and len(result) < k:
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
            i -= 1

        return result