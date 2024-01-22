class Solution:

    # Another DFS + Backtracking solution
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        length = len(nums)

        # Helper DFS function
        def dfs(currSub, index):
            # Add the current subset but do [:] to make a copy
            subsets.append(currSub[:])
            # From index to end of input, append to subset and call DFS
            for i in range(index, length):
                currSub.append(nums[i])
                dfs(currSub, i + 1)
                # Remove from subset for backtracking
                currSub.pop()

        # Driver Code
        dfs([], 0)
        
        return subsets