class Solution:
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_p = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > max_p:
                    max_p = profit
            else:
                left = right
            right = right + 1
            
        return max_p