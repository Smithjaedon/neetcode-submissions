class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxAmount = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit < 0:
                    continue
                maxAmount = max(maxAmount, profit)
        return maxAmount

