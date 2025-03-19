class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {} # checks for row has same number
        col_hash = {} # checks for column has same number
        threeByThreeHash = {} #store a tuple () each 3 by 3 matrix is treated as (row, col) eg: first 3 by 3 matrix as (0,0) - checks for matrix has same number
        for row in range(9):
            for col in range(9):
                if board[row][col] in row_hash.get(row, set()) or board[row][col] in col_hash.get(col,set()) or board[row][col] in threeByThreeHash.get((row//3,col//3), set()):
                    return False
                if board[row][col] != '.':
                    row_hash.setdefault(row, set()).add(board[row][col])
                    col_hash.setdefault(col, set()).add(board[row][col])
                    threeByThreeHash.setdefault((row//3,col//3), set()).add(board[row][col])
        return True
        