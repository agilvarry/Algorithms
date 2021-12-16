#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res_rows = []
        row = 0
        
        while row < numRows:
            new_row = []
            if row == 1:
                new_row.append(1)
            elif row > 1:
                last_row = res_rows[row-1]
                new_row.append(1)
                for i in range(0, len(last_row)-1):
                    j = last_row[i]+last_row[i+1]
                    new_row.append(j)
            new_row.append(1)
            res_rows.append(new_row)
            row += 1
        return res_rows
        