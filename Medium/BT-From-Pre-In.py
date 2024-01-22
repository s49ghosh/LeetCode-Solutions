# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Use a hashmap to map values to indices they appear in the inorder traversal
    #   Turn the preorder traversal into a queue and use it to recursively build up the tree
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            hashmap = {val: i for i,val in enumerate(inorder)}
            preorder = deque(preorder)

            # Helper recursive build function, takes start and end indices 
            #   corresponding to positions in the inorder array
            #   Everything between start and end, inclusive, is part of the subtree
            def buildRec(start, end):
                if start > end: return None
                root = TreeNode(preorder.popleft())
                index = hashmap[root.val]
                root.left = buildRec(start, index - 1)
                root.right = buildRec(index + 1, end)
                return root
            
            return buildRec(0, len(preorder) - 1)