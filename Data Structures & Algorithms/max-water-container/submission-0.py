class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1

        max_area = 0

        while l < r:
            lpeak = heights[l]
            rpeak = heights[r]
            area = (r - l) * min(lpeak, rpeak)
            max_area = max(max_area, area)

            if lpeak <= rpeak:
                l += 1
            else:
                r -= 1
        
        return max_area