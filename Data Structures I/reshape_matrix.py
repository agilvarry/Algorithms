#https://leetcode.com/problems/reshape-the-matrix/
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        old_row =len(mat)
        old_col = len(mat[0])
        res = []
        if r*c != old_row * old_col:
            return mat
        new_row = []
        row_num = 0
        for row in mat:
            for col in row:
                if row_num < c:
                    new_row.append(col)
                    row_num += 1
                if row_num == c:
                    res.append(new_row)
                    new_row = []
                    row_num=0
        return res