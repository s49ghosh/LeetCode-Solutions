# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Do BFS a level at a time
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        ret = []
        queue = deque()
        queue.append(root)
        
        while queue:
            newList = []

            # Need to do the work len(queue) times to ensure we process a whole level at a time
            for _ in range(len(queue)):
                curr = queue.popleft()
                newList.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                
            ret.append(newList)
        
        return ret
