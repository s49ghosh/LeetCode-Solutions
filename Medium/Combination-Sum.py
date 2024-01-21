class Solution:

    # Use DFS and backtracking to explore all combinations. If they sum to the target add to our result
    #   If the sum exceeds our target, we can perform branch pruning and end early
    #   Otherwise, explore further combos
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        ans = []
        
        # Helper DFS function
        def dfs(currentCombo, total, index):
            # Total exceeds target, end early
            if total > target:
                return
            
            # Total equals target, add to ans and return
            if total == target:
                ans.append(currentCombo)
                return
            
            # Total hasnt reached target yet so we need to add more elements to the combo
            #   index remembers how much of the input array we've used already, so we don't reuse
            else:
                for i in range(index, length):
                    dfs(currentCombo + [candidates[i]], total + candidates[i], i)

       # Start DFS with an empty combo, which has a sum of 0, and indicate we've used 0 elements so far 
        dfs([], 0, 0)
        
        return ans