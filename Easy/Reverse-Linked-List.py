# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Traverse list and hash nodes, reconstruct using hashmap
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        hashmap = {}
        i = 0
        
        while head:
            hashmap[i] = head
            i += 1
            head = head.next
        
        i -= 1
        head = hashmap[i]
        
        while i > 0:
            hashmap[i].next = hashmap[i-1]
            i -= 1
        
        hashmap[0].next = None
        return head