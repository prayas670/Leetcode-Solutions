class Solution:
    def partitionLabels(self, s):
        last = [0] * 26

        # Store last occurrence of each character
        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i

        result = []
        start = 0
        end = 0

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')

            if last[index] > end:
                end = last[index]

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result