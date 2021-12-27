#https://leetcode.com/problems/flood-fill/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        l_row, l_col = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        def flood(i,j):
            if image[i][j] == oldColor:
                image[i][j] = newColor
                 #we just just if the 4 directions are in the bounds of 0 and len-1 
                if i >= 1:
                    flood(i-1, j)
                if j >=1:
                    flood(i,j-1)
                if i+1 < l_row:
                    flood(i+1,j)
                if j+1 < l_col:
                    flood(i, j+1)
        flood(sr, sc)
        return image