class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = {}
        for i, point in enumerate(points):
            graph[i] = point

        edges = []
        n = len(points)
        for i in range(n - 1):
            p1 = graph[i]
            for j in range(i+1, n):
                p2 = graph[j]
                d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((d, i, j))
        
        edges.sort()
        rank = [1 for i in range(n)]
        parent = [i for i in range(n)]

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            up, vp = find(u), find(v)
            if up == vp:
                return False
            
            if rank[up] > rank[vp]:
                parent[vp] = up
            elif rank[up] < rank[vp]:
                parent[up] = vp
            else:
                parent[up] = vp
                rank[vp] += 1

            return True
        
        total = 0
        for d, i, j in edges:
            if not union(i, j):
                continue
            else:
                total += d
        
        return total


