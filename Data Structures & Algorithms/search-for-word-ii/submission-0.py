class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = []

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word
        
        res = []
        def dfs(i, j, parent):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            char = board[i][j]
            if char not in parent.children:
                return
            node = parent.children[char]
            if node.word:
                res.append(node.word)
                node.word = None
            
            board[i][j] = '#'
            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)
            board[i][j] = char

            if not node.children and not node.word:
                del parent.children[char]

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)
        
        return res
            
        
