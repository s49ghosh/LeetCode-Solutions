class Solution:

    # Use DP. This is like 0-1 knapsack. We want to select items such that we make a sum of sum(nums) // 2
    #   This is like our weight constraint. For each number, we check every number from the target to the item
    #   and we can either select it or not select it. We can optimize space to use a 1D array instead of a 2D matrix. 
    #   Our recursive relation: dp[num] = dp[num] (not selecting item) or dp[num - item] (selecting item)
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        #  If the total can't be divided by two, we know we can't partition into two equal subsets right away
        if total % 2: return False
        
        target = total // 2
        
        dp = [True] + [False] * (target)
        for item in nums:
            # Need to go from right to left to use a 1D array. 
            #   Left to right would overwrite values we need for next iteration
            for num in range(target, item - 1, -1):
                dp[num] = dp[num] or dp[num - item]
            
            # If we can make target, we can return True early
            if dp[target]: return True
        
        return False