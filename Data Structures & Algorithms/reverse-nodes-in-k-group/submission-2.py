# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseK(start, nodebefore, nodeafter):
            prev = nodeafter
            while start != nodeafter:
                nxt = start.next
                start.next = prev
                prev = start
                start = nxt
            nodebefore.next = prev
        
        count = 0
        dummy = ListNode(0, head)
        trav = head
        nodebefore = dummy
        while trav:
            count += 1
            trav = trav.next
            if count == k:
                nodeafter = trav
                first = nodebefore.next
                reverseK(first, nodebefore, nodeafter)
                nodebefore = first
                count = 0
        
        return dummy.next



