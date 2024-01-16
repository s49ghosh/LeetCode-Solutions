# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Use BST properties. If root is between p and q, they are on either side, so it is the LCA
    #   Otherwise, both are left or both are right, traverse the subtree they are in
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        