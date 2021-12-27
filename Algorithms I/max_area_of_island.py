#https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        l_row, l_col = len(grid), len(grid[0])
        area_max = 0
        seen = set()
        def counting(i,j):
            if 0 <= i < l_row and 0<= j < l_col and (i,j) not in seen:
                seen.add((i,j))
                if grid[i][j]:
                    return 1 + counting(i+1,j) + counting(i-1,j) + counting(i,j+1) + counting(i,j-1)  
            return 0
                    
        for i in range(l_row):
            for j in range(l_col):                
                n=counting(i, j)
                if n > area_max: area_max = n
        
        return area_max