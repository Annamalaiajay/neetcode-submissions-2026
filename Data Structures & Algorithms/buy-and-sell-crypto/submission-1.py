class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for p in prices:
            if p < buy:
                buy = p 
            elif p - buy > profit:
                profit = p - buy 
                
        return profit