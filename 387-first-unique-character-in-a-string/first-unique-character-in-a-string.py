class Solution(object):
    def firstUniqChar(self, s):
        count = [0] * 26

        i = 0
        while i < len(s):
            count[ord(s[i]) - ord('a')] += 1
            i += 1

        i = 0
        while i < len(s):
            if count[ord(s[i]) - ord('a')] == 1:
                return i    

            i += 1
        return -1        