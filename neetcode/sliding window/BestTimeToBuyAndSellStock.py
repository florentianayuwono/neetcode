class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentBuy = 0
        currentSell = 0
        currentProfit = 0
        maxProfit = 0
        i = 0
        j = 1
        while i < len(prices) - 1 and j < len(prices):
            currentSell = prices[j]
            currentBuy = prices[i]
            currentProfit = currentSell - currentBuy
            if currentProfit < 0:
                i = j
                j += 1
            else:
                maxProfit = max(currentProfit, maxProfit)
                j += 1
        return maxProfit