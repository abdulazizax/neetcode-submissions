class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mx = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                mx = max(mx, profit)
            else:
                l = r
            
            r += 1
        
        return mx