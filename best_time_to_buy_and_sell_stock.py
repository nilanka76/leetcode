# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buyPrice = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buyPrice:               
                buyPrice = prices[i]
            else:
                profit = max(profit, prices[i] - buyPrice) 
        return profit

duplicate = Solution()
print(duplicate.maxProfit([7,1,5,3,6,4]))