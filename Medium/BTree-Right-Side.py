# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Do a level-order traversal and simply return the last element of every level
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # No root, return empty list right away
        if not root: return []
        levelOrder = []
        
        queue = deque()
        queue.append(root)

        # BFS to do level-order traversal
        while queue:
            curr = []
            
            # Need to run len(queue) times to evaulate a whole level at a time
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                curr.append(node.val)
            
            levelOrder.append(curr)

        # Return last value in each level
        return [level[-1] for level in levelOrder]
