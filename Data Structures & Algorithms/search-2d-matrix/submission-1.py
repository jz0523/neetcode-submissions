class Solution:
    def binSearch(self, row, l, r, target):
        if l > r:
            return False 
        med = (l + r) // 2
        if row[med] == target:
            return True
        elif target > row[med]:
            return self.binSearch(row, med + 1, r, target)
        else:
            return self.binSearch(row, l, med - 1, target)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        med = len(matrix) // 2
        row = matrix[med]

        if target < row[0]:
            return self.searchMatrix(matrix[:med][:], target)
        elif target > row[-1]:
            return self.searchMatrix(matrix[med+1:][:], target)
        else:
            return self.binSearch(row, 0, len(row) - 1, target)

