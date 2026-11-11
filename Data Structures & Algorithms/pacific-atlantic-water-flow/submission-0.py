class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        reachPacific = set()
        reachAtlantic = set()
        def dfs(i, j, reachOcean, parent):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in reachOcean or heights[i][j] < parent:
                return
            reachOcean.add((i, j))
            h = heights[i][j]
            dfs(i + 1, j, reachOcean, h)
            dfs(i - 1, j, reachOcean, h)
            dfs(i, j + 1, reachOcean, h)
            dfs(i, j - 1, reachOcean, h)
        
        for i in range(ROWS):
                dfs(i, 0, reachPacific, float("-inf"))
                dfs(i, COLS - 1, reachAtlantic, float("-inf"))
        for j in range(COLS):
                dfs(0, j, reachPacific, float("-inf"))
                dfs(ROWS - 1, j, reachAtlantic, float("-inf"))

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in reachPacific and (i, j) in reachAtlantic:
                    res.append(list((i,j)))

        return res

            

