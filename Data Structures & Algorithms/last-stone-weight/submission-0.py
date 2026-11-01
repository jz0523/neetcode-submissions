import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if x > y:
                x -= y
                heapq.heappush(maxheap, -x)
            elif x < y:
                y -= x
                heapq.heappush(maxheap, -y)
        
        return -maxheap[0] if maxheap else 0



