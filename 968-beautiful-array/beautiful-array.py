class Solution:
    def beautifulArray(self, n):
        ans = [1]

        while len(ans) < n:
            temp = []

            # Generate odd numbers
            for x in ans:
                val = 2 * x - 1
                if val <= n:
                    temp.append(val)

            # Generate even numbers
            for x in ans:
                val = 2 * x
                if val <= n:
                    temp.append(val)

            ans = temp

        return ans