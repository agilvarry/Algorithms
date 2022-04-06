#https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:   
        def pascal(prev, idx):
            out = [1]
            for i in range(len(prev)-1):
                out.append(prev[i]+prev[i+1])
            out.append(1)
            
            if idx == rowIndex:
                return out
            else:
                return pascal(out, idx+1)
            
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            return pascal([1,1], 2)
