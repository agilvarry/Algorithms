#https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        l_row, l_col = len(grid), len(grid[0])
        dq = collections.deque()
        fresh = 0
        for r in range(l_row):
            for c in range(l_col):
                if grid[r][c] == 2:
                    dq.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
        days = -1   
        while dq:
            l = len(dq)
            for i in range(l):
                r,c = dq.popleft()
                for d in [(1,0), (0,1), (-1,0), (0,-1)]: #check all adjacent coords 
                    row, col = r + d[0], c+d[1]
                    if 0 <= row < l_row and 0 <= col < l_col and grid[row][col] == 1:
                        grid[row][col] = 2
                        dq.append((row,col))
                        fresh -=1
            days +=1
        if days < 0:
            days = 0
        return days if fresh == 0 else -1
            