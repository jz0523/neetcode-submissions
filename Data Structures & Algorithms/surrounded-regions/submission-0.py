class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited or board[i][j] == 'X':
                return
            
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)
        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS - 1, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        
