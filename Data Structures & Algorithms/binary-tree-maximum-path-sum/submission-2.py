# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')

        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)

            pathsum = leftmax + rightmax + root.val
            leftpathsum = leftmax + root.val
            rightpathsum = rightmax + root.val

            total = max(pathsum, leftpathsum, rightpathsum)
            if total > self.maxsum:
                self.maxsum = total
            
            return max(leftpathsum, rightpathsum, 0)

        dfs(root)
        return self.maxsum