class Solution(object):
    def countCommas(self, n):
        count = 0

        if n >= 1000:
            count += n - 999

        if n >= 1000000:
            count += n - 999999

        if n >= 100000000:
            count += n - 99999999

        return count            
        
        