# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.
# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # For
        # Condition 1 : Each row must contain the digits 1-9 without repetition.
        # Condition 1 : Each column must contain the digits 1-9 without repetition.
        for row in range(9):
            nList = []
            for column in range(9):
                if board[row][column] != ".":
                    if board[row][column] in nList:
                        return False
                    else:
                        nList.append(board[row][column])
        for column in range(9):
            nList = []
            for row in range(9):
                if board[row][column] != ".":
                    if board[row][column] in nList:
                        return False
                    else:
                        nList.append(board[row][column])
        # Condition 3 : Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                # loop for 3 x 3 boxs
                for i in range(3):
                    for j in range(3):
                        current = board[row + i][column + j]
                        if current != ".":
                            nCount = 0
                            # loop for search
                            for k in range(3):
                                for l in range(3):
                                    if board[row + k][column + l] == current:
                                        nCount += 1
                                    if nCount == 2:
                                        return False
                # box = []
                # for i in range(3):
                #     for j in range(3):
                #         current = board[row + i][column + j]
                #         if current != ".":
                #             if current in box:
                #                 return False
                #             else:
                #                 box.append(current)
        return True
# board = [[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]]

# board = [[".",".","4",".",".",".","6","3","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,["5",".",".",".",".",".",".","9","."]
#         ,[".",".",".","5","6",".",".",".","."]
#         ,["4",".","3",".",".",".",".",".","1"]
#         ,[".",".",".","7",".",".",".",".","."]
#         ,[".",".",".","5",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]
#         ,[".",".",".",".",".",".",".",".","."]]

# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]

# board = [[".","8","7","6","5","4","3","2","1"]
#         ,["2",".",".",".",".",".",".",".","."]
#         ,["3",".",".",".",".",".",".",".","."]
#         ,["4",".",".",".",".",".",".",".","."]
#         ,["5",".",".",".",".",".",".",".","."]
#         ,["6",".",".",".",".",".",".",".","."]
#         ,["7",".",".",".",".",".",".",".","."]
#         ,["8",".",".",".",".",".",".",".","."]
#         ,["9",".",".",".",".",".",".",".","."]]

board = [[".",".","5",".",".",".",".",".","."]
        ,[".",".",".","8",".",".",".","3","."]
        ,[".","5",".",".","2",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","."]
        ,[".",".",".",".",".",".",".",".","9"]
        ,[".",".",".",".",".",".","4",".","."]
        ,[".",".",".",".",".",".",".",".","7"]
        ,[".","1",".",".",".",".",".",".","."]
        ,["2","4",".",".",".",".","9",".","."]]

solution = Solution()
print(solution.isValidSudoku(board))