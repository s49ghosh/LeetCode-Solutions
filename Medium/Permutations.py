class Solution:

    # Use DFS with backtracking to find all permutations. Use a Counter to remember which elements have been used
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPerms = []
        length = len(nums)
        counts = Counter(nums)
	
        # Helper DFS
        def dfs(currentPerm):
            # Our perm is same length as input, so we're good to add it to our answer and terminate
            if length == len(currentPerm):
                allPerms.append(currentPerm) 
                return
            
            # Otherwise, we can add more elements
            else:
                # Iterate through or counter dict, if we have an element with a non-zero count, call DFS on it
                for key in counts:
                    if counts[key]:
                        counts[key] -= 1
                        dfs(currentPerm + [key])
                        # Restore count for backtracking
                        counts[key] += 1

        # Driver Code
        dfs([])
        
        return allPerms
