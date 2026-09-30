class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        first_freq = 0

        for ch in freq:
            first_freq = freq[ch]
            break

        for ch in freq:
            if freq[ch] != first_freq:
                return False

        return True                          
        