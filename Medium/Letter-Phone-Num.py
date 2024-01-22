class Solution:

    # Another combination question, so use DFS + Backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        # Digits is the empty str, return early
        if digits == "": return []
        result = []
        digits = deque(digits)
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # Helper DFS function. If digits is empty, we're done and we add the combination to our answer
        #   Otherwise, pop from digits and run DFS on each possible letter that digit maps to
        def dfs(comb, digits):
            if not digits:
                result.append(comb)
                return
        
            curr = digits.popleft()
            for i in range(len(mapping[curr])):
                dfs(comb + mapping[curr][i], digits) 

            digits.appendleft(curr)
        
        # Driver Code
        dfs("", digits)
        
        return result
