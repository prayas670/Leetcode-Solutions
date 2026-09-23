class Solution(object):
    def detectCapitalUse(self, word):
        n = 0
        upper = 0

        for ch in word:
            n += 1
            if 'A' <= ch <= 'Z':
                upper += 1

        if upper == n:
            return True

        if upper == 0:
            return True

        if 'A' <= word[0] <= 'Z' and upper == 1:
            return True

        return False            

        