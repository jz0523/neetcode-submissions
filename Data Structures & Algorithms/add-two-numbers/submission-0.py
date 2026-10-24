# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        head = l1
        multiply = 1
        while head:
            val = head.val
            num1 += multiply * val
            multiply = multiply * 10
            head = head.next
        head = l2
        multiply = 1
        while head:
            val = head.val
            num2 += multiply * val
            multiply = multiply * 10
            head = head.next
        
        res = str(num1 + num2)
        n = len(res)
        dummy = curr = ListNode()
        for i in range(n - 1, -1, -1):
            val = int(res[i])
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next

