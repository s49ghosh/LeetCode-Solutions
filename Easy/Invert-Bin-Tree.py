# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Just recursively call on left and right, and set left to what used to be right
    #   and vice-versa
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # if root is None, return right away
        if not root:
            return root
        
        # Save left in temp as left will be overwritten
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        
        return root
        