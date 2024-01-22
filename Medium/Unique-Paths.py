class Solution:
    
    # Since robot can only move down or right, we can use DP. 
    #   Let dp[i][j] store number of paths to cell[i][j]
    #   Then, dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #   Base Cases: 1 way to get to any cell (i, 0) and (0, j) 
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        # Loop through matrix
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]