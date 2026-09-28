class Solution(object):
    def maxPower(self, s):
        current = 1
        maximum = 1

        i = 1

        while i < len(s):
            if s[i] == s[i - 1]:
                current += 1
            else:
                current = 1

            if current > maximum:
                maximum = current

            i += 1

        return maximum