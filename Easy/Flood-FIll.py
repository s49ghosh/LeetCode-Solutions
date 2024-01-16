class Solution:
    
    # Use BFS. Pop from queue, if inbounds and same color as start, paint
    #   Add adjacent cells to queue
    #   Check if start color is same as given color at the beginning, if so return immediately
    # Beats 99.1%
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color: return image
        
        m = len(image)
        n = len(image[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        queue = deque()
        queue.append((sr, sc))
        
        while queue:
            i, j = queue.popleft()
            
            # Bounds and color check
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != orig:
                continue
            
            image[i][j] = color
            
            # Add adjacent cells to queue
            for dx, dy in directions:
                queue.append((i + dx, j + dy))
        
        return image

        