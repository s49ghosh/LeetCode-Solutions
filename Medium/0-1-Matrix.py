class Solution:

    # Use BFS to search for 1 from each 0
    #   Set every 1 to a large placeholder to indicate they have not been visited
    #   During BFS, if adjacent cell value > current cell + 1, we found a shorter path
    #   Update val and enqueue
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        large = m * n

        # Enqueue all 0s, replace 1s with a large value
        for i in range(m):
            for j in range(n):
                if not mat[i][j]: queue.append((i, j))
                else: mat[i][j] = large
        
        while queue:
            i, j = queue.popleft()
            
            # Consider four-directionally adjacent cells
            for dr, dc in directions:
                newR = i + dr
                newC = j + dc

                # if inbounds and distance larger than current cell's distance, update and enqueue
                if 0 <= newR < m and 0 <= newC < n and mat[newR][newC] > mat[i][j] + 1:
                    mat[newR][newC] = mat[i][j] + 1
                    queue.append((newR, newC))
        
        return mat