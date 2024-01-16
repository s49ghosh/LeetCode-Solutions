# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # Use a set, since nodes are hashable. If we see a node in the set, we have a cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        
        while head:
            if head in nodeSet:
                return True
            
            nodeSet.add(head)
            head = head.next
        
        return False