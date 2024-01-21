# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Traverse the tree. If at any point, left and right return true, 
    #   p and q are on different subtrees of the current node, so current node is the LCA
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        # We found one of the nodes, return root
        if root == p or root == q: return root

        # Recurse on left and right
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # If both l and r are true, root is LCA
        if l and r: return root
        # Otherwise, return the one which is not none
        return l or r