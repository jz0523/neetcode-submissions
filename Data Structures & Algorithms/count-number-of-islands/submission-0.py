from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def bfs(r, c):
            seen.add((r, c))
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0" or (r, c) in seen:
                    continue
                else:
                    bfs(r, c)
                    islands += 1
        
        return islands


