# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        valToIdx = {}
        for i, val in enumerate(inorder):
            valToIdx[val] = i
        
        self.pre_idx = 0
        def build(l, r):
            if l > r:
                return None
            
            rootval = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(rootval)
            mid = valToIdx[rootval]

            root.left = build(l, mid - 1)
            root.right = build(mid+1, r)

            return root
        
        return build(0, len(inorder) - 1)
