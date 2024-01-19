class Solution:

    # Kadane's Algo: DP where dp[i] = max(dp[i - 1] + nums[i], nums[i])
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * n
        sums[0] = nums[0]
        
        # sums[i] = sums[i - 1] + nums[i] if nums[i] > 0
        #   If it isn't, adding it would decrease our sum, so we start a new sum with nums[i]
        for i in range(1, n):
            sums[i] = max(sums[i - 1] + nums[i], nums[i])
        
        return max(sums)
        
