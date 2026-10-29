class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 0
        profit = 0
        for idx, item in enumerate(prices):
            if item < prices[minimum]:
                minimum = idx
            new_profit = item - prices[minimum]
            if new_profit > profit:
                profit = new_profit

        return profit            