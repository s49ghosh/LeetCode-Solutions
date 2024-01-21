# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # An Inorder traversal of a valid BST gives a non-decreasing array
    #   So do an inorder traversal, and validate the resultant is non-decreasing
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        nums = []
        
        # Helper inorder traversal function
        def inOrderTrav(root):
            if not root: return
            inOrderTrav(root.left)
            nums.append(root.val)
            inOrderTrav(root.right)
        
        inOrderTrav(root)

        # Traverse the array, if it is non-decreasing, the BST is invalid
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]: return False
        
        return True
            

        