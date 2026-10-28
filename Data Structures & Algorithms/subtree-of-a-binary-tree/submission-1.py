# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSame(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2 or root1.val != root2.val:
                return False

            return checkSame(root1.left, root2.left) and checkSame(root1.right, root2.right)
        
        if not root:
            return False

        if checkSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        

        

        
