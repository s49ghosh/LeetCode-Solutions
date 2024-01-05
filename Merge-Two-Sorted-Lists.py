# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Approach: List1 and List2 are sorted, so while both have elements, add smaller of their heads to the list
    #   After, if either list still has elements, simply append them to the end
    #   Use a dummy node to avoid convoluted logic to take care of the head
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy

        # Both lists have elements
        while list1 and list2:
            # Pick smaller
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # One or None of the lists have elements left
        # If one of them does, append them to our merged list
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        return dummy.next