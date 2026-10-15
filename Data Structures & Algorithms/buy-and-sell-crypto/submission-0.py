class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        maxP = 0

        while s < len(prices):
            if prices[s] > prices[b]:
                maxP = max(maxP, prices[s] - prices[b])
            else:
                b = s
            s += 1
        
        return maxP
