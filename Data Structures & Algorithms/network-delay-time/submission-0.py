from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        
        heap = [(0, k)]
        total = 0

        visited = set()

        while heap:
            d, v = heapq.heappop(heap)
            if v in visited:
                continue

            total = d
            visited.add(v)

            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(heap, (d + w, neighbor))
            

        return total if len(visited) == n else -1


