class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        squares = [[] for _ in range(9)] # 9 for each 3x3 square
        colarray = [[] for _ in range(9)]
        for r in range(rows):
            rowsarray = []
            for c in range(cols):
                if board[r][c] in rowsarray:
                    return False
                else:
                    if board[r][c] >= '1' and board[r][c] <= '9':
                        rowsarray.append(board[r][c])
                if board[r][c] in colarray[c]:
                    return False
                else:
                    if board[r][c] >= '1' and board[r][c] <= '9':
                        colarray[c].append(board[r][c]) 
                
                rowsquare = r // 3
                colsquare = c // 3
                square_index = rowsquare * 3 + colsquare
                print("rowsquare:", rowsquare)
                print("colsquare:", colsquare)
                if board[r][c] in squares[square_index]:
                    print("square false")
                    return False
                else:
                    if board[r][c] >= '1' and board[r][c] <= '9':
                        squares[square_index].append(board[r][c])
                        print("quares[colsquare + rowsquare]:", squares[square_index])
        
        return True
