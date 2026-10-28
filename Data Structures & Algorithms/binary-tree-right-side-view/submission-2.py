# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        if not root:
            return res

        while q:
            qlen = len(q)
            res.append(q[-1].val)
            for i in range(qlen):
                node = q.popleft()
                left = node.left
                right = node.right
                if left:
                    q.append(left)
                if right:
                    q.append(right)
            
        return res