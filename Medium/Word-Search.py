class Solution:

    # Look for the first char in the word, then do DFS to try and find the rest
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Deque for easy pops and appends to left
        word = deque(word)
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Helper DFS function, given a cell (i,j) and a word, tries to find the word from the cell
        def dfs(i, j, word):
            if not word: return True

            # If out of bounds or the cell does not match the first char in the word, return early
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
                return
            
            # If it does match, set cell to a special char so we don't use it again
            board[i][j] = '#'
            char = word.popleft()

            # Call DFS four-directionally
            for dx, dy in directions:
                # If we find the word, return True
                if dfs(i + dx, j + dy, word): 
                    return True
            
            # Reset word and board for backtracking
            word.appendleft(char)
            board[i][j] = char
                
        # Iterate through matrix looking for first char in word
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        
        return False