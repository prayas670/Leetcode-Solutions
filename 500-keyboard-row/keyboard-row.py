class Solution:
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"

        result = []

        for word in words:
            row = 0
            valid = True

            for ch in word:
                i = 0
                while i < 26:
                    if ch == upper[i]:
                        ch = lower[i]
                        break
                    i += 1

                if ch in row1:
                    if row == 0:
                        row = 1
                    elif row != 1:
                        valid = False
                        break

                elif ch in row2:
                    if row == 0:
                        row = 2
                    elif row != 2:
                        valid = False
                        break

                elif ch in row3:
                    if row == 0:
                        row = 3
                    elif row != 3:
                        valid = False
                        break

            if valid:
                result.append(word)

        return result