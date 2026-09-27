class Solution(object):
    def reverseWords(self, s):
        words = []
        word = ""

        for ch in s:
            if ch != ' ':
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""

        if word != "":
            words.append(word)

        count = 0
        for x in words:
            count += 1

        result = ""
        i = count - 1

        while i >= 0:
            result += words[i]

            if i > 0:
                result += " "

            i -= 1
            
        return result        