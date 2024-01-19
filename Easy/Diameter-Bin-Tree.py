# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    # At each node calculate diameter (height of left + height of right) and store, return max at end
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        paths = []
        
        def height(node):
            left = height(node.left) if node.left else 0
            right = height(node.right) if node.right else 0
            paths.append(left + right)
            
            if left > right: return left + 1
            return right + 1
        
        height(root)
        
        return max(paths)

        