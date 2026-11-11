from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = set()
        path = set()
        def dfs(v):
            if v in path:
                return False
            if v in visited:
                return True
            
            path.add(v)

            for neighbor in graph[v]:
                if not dfs(neighbor):
                    return False
            path.remove(v)

            visited.add(v)
            
            return True
        
        for v in range(numCourses):
            if v not in visited:
                if not dfs(v):
                    return False
        
        return True
