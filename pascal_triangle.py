# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        triangle.append([1])
        if numRows == 1:
            return triangle
        triangle.append([1,1])
        if numRows == 2:
            return triangle
        else:
            for i in range(1, numRows-1):
                currentLi = [1]
                for j in range(0, i):
                    currentLi.append(triangle[i][j] + triangle[i][j+1])
                currentLi.append(1)
                triangle.append(currentLi)
            return triangle
solution = Solution()
print(solution.generate(6))