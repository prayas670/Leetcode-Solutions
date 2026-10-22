class Solution:
    def removeStars(self, s):
        stack = [''] * len(s)
        top = 0

        for ch in s:
            if ch == '*':
                top -= 1
            else:
                stack[top] = ch
                top += 1

        result = ""
        i = 0

        while i < top:
            result += stack[i]
            i += 1

        return result