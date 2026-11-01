import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x**2 + y**2)
            if len(maxheap) < k:
                heapq.heappush(maxheap, (-dist, point))
            else:
                if dist < -maxheap[0][0]:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, (-dist, point))
        
        return [pair[1] for pair in maxheap]