class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxarea = 0
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited:
                return 0
            cell = grid[i][j]
            visited.add((i,j))
            if cell == 0:
                return 0
            res = 1
            res += dfs(i + 1, j)
            res += dfs(i - 1, j)
            res += dfs(i, j + 1)
            res += dfs(i, j - 1)

            return res
        for i in range(ROWS):
            for j in range(COLS):
                area = dfs(i, j)
                maxarea = max(area, maxarea)
        
        return maxarea