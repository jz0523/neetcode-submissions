class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for i in range(n)]
        col = set()
        negdiag = set()
        posdiag = set()

        def dfs(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r - c) in negdiag or (r + c) in posdiag:
                    continue
                
                #choose this col to put the Queen
                board[r][c] = "Q"
                col.add(c)
                negdiag.add(r - c)
                posdiag.add(r + c)

                dfs(r + 1)
                #recover the original board
                board[r][c] = "."
                col.remove(c)
                negdiag.remove(r - c)
                posdiag.remove(r + c) 
        
        dfs(0)
        return res


