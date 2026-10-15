class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        count = 0
        leftMax, rightMax = height[l], height[r]
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                count += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                count += rightMax - height[r]

        return count






            