class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] > prices[i]:
        #             profit = prices[j] - prices[i]
        #             max_profit = max(profit, max_profit)             
        # return max_profit

        # l = 0
        # r = l + 1
        # max_profit = 0

        # while l < len(prices) and r < len(prices):
        #     profit = prices[r] - prices[l]
        #     if prices[r] >= prices[l]:
        #         max_profit = max(profit, max_profit)
        #         r += 1
        #     else:
        #         l += 1 
        #         r = l + 1
        # return max_profit   

        max_P = 0
        minBuy = prices[0]

        for sell in prices:
            max_P = max(max_P, sell - minBuy)
            minBuy = min(minBuy, sell)
        return max_P

            




