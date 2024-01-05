class Solution:
    
    # We can do a singular pass and update the maximum profit and minimum price at each iteration
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # minPrice starts at the first possible price
        minPrice = prices[0]

        for i in prices:
            profit = max(i - minPrice, profit)
            minPrice = min(i, minPrice)
        
        return profit