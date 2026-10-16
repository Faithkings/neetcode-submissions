class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] > prices[j]:
                    profit = 0
                    max_profit = max(profit, max_profit)
                elif prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    max_profit = max(profit, max_profit)
                    
        return max_profit


