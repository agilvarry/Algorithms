#https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = len(matrix)
        for i in range(l):
            if i+1 == l:
                return self.searchRow(matrix[i], target) 
            if matrix[i][0] <= target and matrix[i+1][0] > target:
                return self.searchRow(matrix[i], target)    
    
    
    def searchRow(self, row: List, target: int) -> bool:
        if target in row:
            return True
        else:
            return False