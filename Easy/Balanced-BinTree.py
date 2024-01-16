# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Traverse tree and check height at each node
    #   If one is imbalanced, pass -1 up to indicate there is an imbalance
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left, right = height(root.left), height(root.right)
            
            if left < 0 or right < 0 or abs(left - right) > 1: return -1
            
            return 1 + max(left, right)
        
        return height(root) >= 0
        