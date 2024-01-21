class Solution:
    
    # Search for a rotting orange, use BFS to find all fresh oranges it can rot and the shortest path to them
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        maximum = 0
        
        queue = deque()

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        # Traverse matrix and add all rotten oranges to the queue
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 2:
                    for dx, dy in directions:
                        queue.append((i + dx, j + dy, 1))

        # BFS
        while queue:
            row, col, count = queue.popleft()
            # If out of bounds or not a fresh orange, we can return right away
            if row < 0 or row >= numRows or col < 0 or col >= numCols or grid[row][col] != 1:
                continue

            # Set the fresh orange to a rotten one
            grid[row][col] = 2
            maximum = max(maximum, count)

            for dx, dy in directions:
                queue.append((row + dx, col + dy, count + 1))
            
        # Check if any fresh oranges did not rot
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1: return -1
        
        return maximum



        
        
