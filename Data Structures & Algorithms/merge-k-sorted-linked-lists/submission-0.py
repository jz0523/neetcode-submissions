# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedlist = []
            for i in range(0, len(lists), 2):
                head1 = lists[i]
                head2 = lists[i + 1] if i + 1 < len(lists) else None
                merged = self.mergeTwoList(head1, head2)
                mergedlist.append(merged)
            lists = mergedlist
        
        return lists[0] if lists else None
            
        

    def mergeTwoList(self, head1, head2):
        a, b = head1, head2
        dummy = head = ListNode()
        while a and b:
            if a.val < b.val:
                head.next = a
                head = head.next
                a = a.next
            else:
                head.next = b
                head = head.next
                b = b.next
        head.next = a or b

        return dummy.next
