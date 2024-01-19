# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    # Hash nodes while keeping track of index
    #   At the end, i is length, return node @ i // 2
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        hashmap = {}
        
        while head:
            hashmap[i] = head
            head = head.next
            i += 1
        
        return hashmap[i // 2]
