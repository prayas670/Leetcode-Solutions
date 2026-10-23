class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = [0] * n
        top = -1
        i = 0

        while i < n:
            while top >= 0 and temperatures[i] > temperatures[stack[top]]:
                index = stack[top]
                top -= 1
                result[index] = i - index

            top += 1
            stack[top] = i
            i += 1

        return result