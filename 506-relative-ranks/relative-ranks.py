class Solution:
    def findRelativeRanks(self, score):
        n = len(score)

        arr = []

        # Store scores and original indices
        for i in range(n):
            arr.append([score[i], i])

        # Sort in descending order using Bubble Sort
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j][0] < arr[j + 1][0]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

        # Create answer array
        ans = [""] * n

        # Assign ranks
        for i in range(n):
            index = arr[i][1]

            if i == 0:
                ans[index] = "Gold Medal"
            elif i == 1:
                ans[index] = "Silver Medal"
            elif i == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(i + 1)

        return ans