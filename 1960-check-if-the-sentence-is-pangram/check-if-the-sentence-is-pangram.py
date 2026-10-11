class Solution(object):
    def checkIfPangram(self, sentence):
        letters = [False] * 26

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for ch in sentence:
            i = 0

            while i < 26:
                if ch == alphabet[i]:
                    letters[i] = True
                    break
                i += 1

        for i in range(26):
            if letters[i] == False:
                return False
        return True                    
        