class Solution(object):
    def largestGoodInteger(self, num):
        largest = ""

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                current = num[i] * 3

                if largest == "" or current > largest:
                    largest = current

        return largest            


        