# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:

        # reshapedMat = [[0]*c for i in range(r)] # Don't use [[v]*n]*n, it is a trap!
        # matValues = []
        # for row in mat:
        #     for column in row:
        #         matValues.append(column)

        # index = 0
        # if r * c == len(matValues):
        #     for row in range(r):
        #         for column in range(c):
        #             reshapedMat[row][column] = matValues[index]
        #             index += 1
        #     return reshapedMat
        # else:
        #     return mat

        reshapedMat = []
        matValues = sum(mat, [])
        
        if r * c == len(matValues):
            for i in range(0,len(matValues),c):
                reshapedMat.append(matValues[i:i+c])
            return reshapedMat
        else:
            return mat

solution = Solution()
mat =[[1,2], [3,5], [7,6]]
r, c = 2 , 3
print(mat)
print(solution.matrixReshape(mat, r, c))