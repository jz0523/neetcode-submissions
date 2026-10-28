# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.anc = None

        def traverse(root, p, q):
            if not root:
                return False
            
            if root.val == p.val:
                self.anc = p
            elif root.val == q.val:
                self.anc = q
            elif p.val > root.val and q.val > root.val:
                return traverse(root.right, p, q)
            elif p.val < root.val and q.val < root.val:
                return traverse(root.left, p, q)
            else:
                self.anc = root
                return True
            
        traverse(root, p, q)

        return self.anc