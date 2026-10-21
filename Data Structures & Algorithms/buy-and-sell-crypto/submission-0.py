class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minp = prices[0]

        for i in range(len(prices)):
            curp = prices[i] - minp
            if curp>profit:
                profit = curp
            minp = min(minp,prices[i])
        return profit