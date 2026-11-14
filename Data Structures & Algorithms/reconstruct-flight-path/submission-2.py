from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse = True)
        for u, v in tickets:
            graph[u].append(v)
        
        res = []
        def dfs(v):
            while graph[v]:
                w = graph[v].pop()
                dfs(w)
            res.append(v)
        
        dfs("JFK")
        return res[::-1]
