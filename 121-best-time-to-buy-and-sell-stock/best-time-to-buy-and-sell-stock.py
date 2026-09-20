class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]

            current_profit = prices[i] - buy

            if current_profit > profit:
                profit =  current_profit

        return profit    
        