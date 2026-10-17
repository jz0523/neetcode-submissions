class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                start = idx

            stack.append((start, height))
        
        for bar in stack:
            max_area = max(max_area, bar[1] * (len(heights) - bar[0]))
        
        return max_area



