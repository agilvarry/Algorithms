#https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) !=9 or len(board[0]) != 9:
            return False
        
        return self.row_check(board) and self.column_check(board) and self.box_check(board)
    
    def row_check(self, board):
        for i in board:
            if not self.check_repetition(i): 
                return False
        return True
    
    def column_check(self, board):
        for i in zip(*board):
            if not self.check_repetition(i): 
                return False
        return True
        
    def box_check(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.check_repetition(square):
                    return False
        return True
        
    def check_repetition(self, group: list[str]) -> bool:
        seen = {}
        for i in group:
            if i == ".":
                continue
            elif i.isnumeric() and i not in seen:
                seen[i] =1
            else: return False
        return True        