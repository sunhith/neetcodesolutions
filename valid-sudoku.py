class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = set()
        col_hash = set()
        threeByThreeHash = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] in row_hash and board[row][col] in col_hash and board[row][col] in threeByThreeHash.get((int(row/3),int(col/3)), set()):
                    return False
                row_hash.add(board[row][col])
                col_hash.add(board[row][col])
                threeByThreeHash.get((int(row/3),int(col/3)),set()).add(board[row][col])
        return True
        