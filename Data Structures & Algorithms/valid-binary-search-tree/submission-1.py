# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValid(node, up, low):
            if not node:
                return True
            elif not (low < node.val < up):
                return False
            else:
                return checkValid(node.left, node.val, low) and checkValid(node.right, up, node.val)
        
        
        up = float('inf')
        low = float('-inf')

        return checkValid(root, up, low)