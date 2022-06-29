# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#               Integers in each row are sorted from left to right.
#               The first integer of each row is greater than the last integer of the previous row.
# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        row = None
        while start <= end :
            mid = (start + end)//2
            if target >= matrix[mid][0] and (mid == end):
                row = mid
                break
            elif target < matrix[mid][0]:
                end = mid - 1
            elif target >= matrix[mid][0] and target < matrix[mid + 1][0]:
                row = mid
                break
            else:
                start = mid + 1
        if row == None:
            return False
        start = 0
        end = len(matrix[row]) - 1
        column = None
        while start <= end:
            mid = (start + end)//2
            if target < matrix[row][mid]:
                end = mid - 1
            elif target == matrix[row][mid]:
                return True
            else:
                start = mid + 1
        return False

matrix =[[ 1, 3, 5, 7]
        ,[10,11,16,20]
        ,[23,30,34,60]
        ,[70,80,90,100]
        ,[120,130,130,150]
        ,[170,200,300,500]]
target = 200
solution = Solution()
print(solution.searchMatrix(matrix , target))
