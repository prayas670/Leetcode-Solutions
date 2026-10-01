class Solution(object):
    def halvesAreAlike(self, s):
        mid = len(s) // 2

        first = 0
        second = 0

        vowels = "aeiouAEIOU"

        i = 0
        while i < mid:
            j = 0

            while j < len(vowels):
                if s[i] == vowels[j]:
                    first += 1
                    break

                j += 1
            
            i += 1

        i = mid
        while i < len(s):
            j = 0

            while j < len(vowels):
                if s[i] == vowels[j]:
                    second += 1
                    break

                j += 1

            i += 1

        return first == second                        
        