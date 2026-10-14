from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                elm = board[i][j]
                if elm == ".":
                    continue
                box = (i // 3, j // 3)
                if elm in rows[i] or elm in cols[j] or elm in boxes[box]:
                    return False
                else:
                    rows[i].add(elm)
                    cols[j].add(elm)
                    boxes[box].add(elm)
        
        return True