from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        time = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
        
        def addCell(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i,j) in visited or grid[i][j] == 0:
                return
            q.append((i, j))
            visited.add((i, j))
        
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                addCell(i+1, j)
                addCell(i-1, j)
                addCell(i, j+1)
                addCell(i, j-1)
            if q:
                time += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return -1
        
        return time

        