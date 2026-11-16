import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        direction = [[0,1], [0, -1], [1, 0], [-1, 0]]
        heap = [(grid[0][0], 0, 0)]

        visited.add((0, 0))

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in direction:
                newR, newC = r + dr, c + dc
                if newR < 0 or newR == n or newC < 0 or newC == n or (newR, newC) in visited:
                    continue
                visited.add((newR, newC))
                heapq.heappush(heap, (max(t, grid[newR][newC]), newR, newC))
    


