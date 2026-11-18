class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src] = 0
        
        for _ in range(k + 1):
            tempprices = prices.copy()
            for u, v, w in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u] + w < tempprices[v]:
                    tempprices[v] = prices[u] + w
            
            for i in range(n):
                prices[i] = tempprices[i]
            
        return prices[dst] if prices[dst] != float("inf") else -1