class Solution:

    # Use DP to find the max we can steal.
    #   Let DP[i] contain max we can still from first i + 1 houses
    #   Base Cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
    #   Recursive Relation: dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    def rob(self, nums: List[int]) -> int:
        dp = []
        length = len(nums)

        # If only one house, rob it..
        if length == 1: 
            return nums[0]
        
        dp.append(nums[0])
        maxFirstTwo = max(nums[0], nums[1])

        # If only two houses, rob the better one
        if length == 2:
            return maxFirstTwo
        
        dp.append(maxFirstTwo)
        
        # Calculate recursive relation
        for i in range(2, length):
            maximum = max(nums[i] + dp[i - 2], dp[i - 1])
            dp.append(maximum)
        
        # Max we can get from first 'length' houses, our final answer
        return dp[length - 1]
