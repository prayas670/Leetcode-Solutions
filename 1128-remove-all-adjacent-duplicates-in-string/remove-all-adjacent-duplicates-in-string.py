class Solution:
    def removeDuplicates(self, s):
        n = 0
        for ch in s:
            n += 1

        stack = [""] * n
        top = -1

        i = 0
        while i < n:
            if top >= 0 and stack[top] == s[i]:
                top -= 1
            else:
                top += 1
                stack[top] = s[i]
            i += 1

        result = ""
        i = 0
        while i <= top:
            result += stack[i]
            i += 1

        return result