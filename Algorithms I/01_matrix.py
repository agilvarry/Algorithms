#https://leetcode.com/problems/01-matrix/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        l_row, l_col = len(mat), len(mat[0])
        seen = set()
        dq= collections.deque()
        # we collect all the coordinates of the 0's
        for i in range(l_row):
            for j in range(l_col): 
                if mat[i][j] == 0:
                    seen.add((i,j))
                    dq.append((i,j))
                    
        while dq: #iterate over the queue, initially just the 0's
            i,j = dq.popleft()
            for d in [(1,0), (0,1), (-1,0), (0,-1)]: #check all adjacent coords 
                x,y = i + d[0], j+d[1]
                if (x,y) not in seen and 0 <= x < l_row and 0 <= y < l_col: #if x,y is on the mat and hasn't been seen
                    mat[x][y] = mat[i][j] + 1 #distance from 0 of x,y is i,j +1
                    seen.add((x,y))
                    dq.append((x,y)) #add the newly seen non-0 locations to the queue
        return mat