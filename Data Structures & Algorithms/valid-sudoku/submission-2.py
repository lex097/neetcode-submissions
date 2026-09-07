class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows and columns
        for i in range(9):
            rowMap = {}
            colMap = {}
            for j in range(9):
                # check row
                if board[i][j] != ".":
                    if board[i][j] in rowMap:
                        return False
                    rowMap[board[i][j]] = 1
                
                # check column
                if board[j][i] != ".":
                    if board[j][i] in colMap:
                        return False
                    colMap[board[j][i]] = 1
        
        # check 3x3 sub-boxes
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                boxMap = {}
                for i in range(boxRow, boxRow + 3):
                    for j in range(boxCol, boxCol + 3):
                        if board[i][j] != ".":
                            if board[i][j] in boxMap:
                                return False
                            boxMap[board[i][j]] = 1
        
        return True
