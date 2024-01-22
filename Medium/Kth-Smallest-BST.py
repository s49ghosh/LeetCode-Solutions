# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Like validating a BST, note an Inorder traversal of a BST finds items in non-decreasing order
    #   So do an inorder traversal, and when we find kth smallest, terminate
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.ans = -1

        # Helper inorder traversal function
        def inOrder(root):
            if not root: return False
            # If kth smallest is in left subtree, return true
            if inOrder(root.left): return True

            # Else, decrement count to indicate we found an element before the kth smallest
            self.count -= 1

            # If count hits 0, root is kth smallest
            if not self.count:
                self.ans = root.val
                return True

            # If kth smallest is in the right subtree, return True
            if inOrder(root.right): return True

            # Not in either subtree or root
            return False
        
        # Driver code
        inOrder(root)

        return self.ans
            