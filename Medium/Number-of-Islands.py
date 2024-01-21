class Solution:
    
    # Approach: Traverse the matrix, look for an island. When we find one increment count and use DFS to find the rest of it
    #   and set the whole island to 0.
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        count = 0
        m = len(grid)
        n = len(grid[0])

        # Helper dfs function, i is row index, j is col index
        def dfs(i, j):
            # if cell is out of bounds or not part of an island, we can return early
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1': return

            # Set cell to 0 so we don't revisit, call dfs four-directionally
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Traverse matrix looking for islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    
        return count
