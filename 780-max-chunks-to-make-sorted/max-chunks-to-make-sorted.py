class Solution:
    def maxChunksToSorted(self, arr):
        count = 0
        max_val = 0

        for i in range(len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]

            if max_val == i:
                count += 1

        return count