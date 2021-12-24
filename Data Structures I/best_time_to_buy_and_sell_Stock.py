#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        large, small = prices[0], prices[0]
        best = 0
        for i in prices:
            if i < small:
                small, large = i, i
            elif i > large:
                large = i
                
            if large - small > best:
                best = large - small
                
        return best
        
