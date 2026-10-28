# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        currmax = float('-inf')
        self.res = 0
        def dfs(root, currmax):
            if not root:
                return
            
            if root.val >= currmax:
                currmax = root.val
                self.res += 1
            
            dfs(root.left, currmax)
            dfs(root.right, currmax)
        
        dfs(root, currmax)
        return self.res
