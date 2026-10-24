# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        length = 0
        while start:
            length += 1
            start = start.next
        
        idx = length - n
        if idx == 0:
            return head.next

        curr_idx = 0
        curr = head
        prev = ListNode()
        while curr and curr_idx != idx:
            curr_idx += 1
            prev = curr
            curr = curr.next

        nxt = curr.next
        prev.next = nxt
        
        return head
