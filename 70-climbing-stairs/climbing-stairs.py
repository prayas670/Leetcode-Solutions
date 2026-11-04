class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        a = 1
        b = 2

        i = 3
        while i <= n:
            c = a + b
            a = b
            b = c
            i += 1

        return b