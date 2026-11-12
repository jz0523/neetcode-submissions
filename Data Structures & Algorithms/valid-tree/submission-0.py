from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [[] for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        
        def dfs(v, p):
            if v in visited:
                return False
            
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor == p:
                    continue
                if not dfs(neighbor, v):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n

            

        
