class Solution(object):
    def generateTheString(self, n):
        result = ""

        if n % 2 == 1:
            for i in range(n):
                result += "a"

        else:
            for i in range(n - 1):
                result += "a"

            result += "b"
        return result                